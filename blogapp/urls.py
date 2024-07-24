from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, register, CustomAuthToken
router = DefaultRouter()
router.register(r'posts', PostViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('register/', register, name='register'),
    path('api-token-auth/', CustomAuthToken.as_view(), name='api_token_auth'),
]