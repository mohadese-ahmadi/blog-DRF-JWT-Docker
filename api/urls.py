from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BlogViewSets, CategoryViewSet, TagViewSets
router=DefaultRouter()
router.register('post', BlogViewSets)
router.register('tag', CategoryViewSet)
router.register('category', TagViewSets)
urlpatterns=[
    path('',include(router.urls)),
]