from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView,)
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from .views import BlogViewSets, CategoryViewSet, TagViewSets, RegisterView
router = DefaultRouter()
router.register('post', BlogViewSets)
router.register('category', CategoryViewSet)
router.register('tag', TagViewSets)
urlpatterns = [
    path(
        '',
        include(
            router.urls)),
    path(
        'token/',
        TokenObtainPairView.as_view(),
        name='token_obtain_pair'),
    path(
        'token/refresh/',
        TokenRefreshView.as_view(),
        name='token_refresh'),
    path(
        "register/",
        RegisterView.as_view(),
        name="register"),
    path(
        'schema/',
        SpectacularAPIView.as_view(),
        name='schema'),
    path(
        'schema/swagger/',
        SpectacularSwaggerView.as_view(
            url_name='schema'),
        name='swagger-ui'),
    path(
        'schema/redoc/',
        SpectacularRedocView.as_view(
            url_name='schema'),
        name='redoc'),
]
