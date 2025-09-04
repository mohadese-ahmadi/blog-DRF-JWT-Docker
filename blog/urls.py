from django.urls import path
from . import views as v
urlpatterns = [
    path(
        '',
        v.HomeView,
        name='home'),
    path(
        'post-list/',
        v.BlogsList.as_view(),
        name='post-list'),
    path(
        'post-list/<int:pk>',
        v.BlogsDetailView.as_view(),
        name='post-detail'),
    path(
        'post-list/<int:pk>/delete',
        v.BlogsDeleteView.as_view(),
        name='post-delete'),
    path(
        'post-list/<int:pk>/update',
        v.BlogsUpdateView.as_view(),
        name='post-update'),
    path(
        'post-list/add/',
        v.BlogsCreateView.as_view(),
        name='post-add'),
    path(
        'blogs/category/<int:category_id>/',
        v.blog_by_category,
        name='blog_by_category'),
]
