from django.urls import path
from django.contrib.auth import views as auth_views
from . import views as v
urlpatterns = [
    path(
        'login/',
        auth_views.LoginView.as_view(
            template_name='account/login.html',
            next_page='home'),
        name='login'),
    path(
        'logout/',
        auth_views.LogoutView.as_view(
            next_page='home'),
        name='logout'),
    path(
        'register/',
        v.registerView,
        name='register'),
]
