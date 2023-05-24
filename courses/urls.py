from django.urls import path, include
from . import views
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('', login_required(views.courses), name='courses'),
    path('<int:pk>', login_required(views.CourseDetailView.as_view()), name='course_detail'),
    path('<int:course_id>/enroll', views.enroll_course, name='enroll_course'),
    path('<int:course_id>/material', views.course_materials, name='course_materials'),
]