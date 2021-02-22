from django.contrib.auth.models import User
from rest_framework import serializers

from person.models import Post, Like
from person.validators import email_validation


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'url', 'author', 'content', 'created_at', 'draft')
        extra_kwargs = {
            'url': {'read_only': True},
        }


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=False, allow_blank=True)

    def validate_email(self, value):
        """
        Check that the email is verified
        """
        if not email_validation(value):
            raise serializers.ValidationError("Email doesn't verified")
        return value

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ('like',)
