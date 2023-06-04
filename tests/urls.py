from django.urls import path, include
from . import views
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('<int:test_id>/', views.test_detail, name='test_detail'),
    path('<int:test_id>/submit', views.submit_answers, name='submit_answers'),
]