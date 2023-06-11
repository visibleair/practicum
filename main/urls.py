from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('register', views.register, name='register'),
    path('login', views.user_login, name='login'),
    path('profile/edit', views.edit_profile, name='profile_edit'),
]