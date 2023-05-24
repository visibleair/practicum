from django.urls import path, include
from . import views
from .views import register, user_login

urlpatterns = [
    path('', views.index, name='home'),
    path('profile', views.profile, name='profile'),
    path('register', views.register, name='register'),
    path('login', views.user_login, name='login'),
    path('profile/edit', views.edit_profile, name='profile_edit'),
]