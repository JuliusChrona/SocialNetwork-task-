from django.urls import path
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import PostViewSet, UserView, LikeView, UserLoginView

router = SimpleRouter()

router.register(r'post', PostViewSet)
router.register(r'user', UserView)
router.register(r'like', LikeView)

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('user/login/', UserLoginView.as_view(), name='api_login')
]

urlpatterns += router.urls
