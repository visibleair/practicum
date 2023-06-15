from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='home'),
    path('register', views.register, name='register'),
    path('login', views.user_login, name='login'),
    path('profile/edit', views.edit_profile, name='profile_edit'),
]