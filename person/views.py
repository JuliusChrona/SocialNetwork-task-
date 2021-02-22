import time

from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.utils.text import slugify
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from person.models import Post, Like
from person.serializers import PostSerializer, UserSerializer, LikeSerializer


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend]

    filter_fields = ['draft']
    search_fields = ['author', 'title']
    ordering_fields = ['author', 'title', 'created_at']

    def perform_create(self, serializer):
        serializer.validated_data['author'] = self.request.user
        serializer.validated_data['url'] = slugify(serializer.validated_data['title'] + str(round(time.time())))
        serializer.save()


class LikeView(mixins.UpdateModelMixin, GenericViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    lookup_field = 'post'

    def get_object(self):
        obj, _ = Like.objects.get_or_create(user=self.request.user, post_id=self.kwargs['post'])
        return obj


class UserView(mixins.CreateModelMixin, GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = []


class UserLoginView(APIView):
    permission_classes = []

    def post(self, request, *args, **kwargs):
        user = authenticate(username=request.data['username'], password=request.data['password'])
        if user is not None:
            login(request, user)
            response = {
                "message": "successful login"
            }
        else:
            response = {
                "error_message": "invalid credentials"
            }
        return Response(response)
