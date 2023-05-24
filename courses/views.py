from django.shortcuts import render, get_object_or_404, redirect
from .models import Course, CourseMaterial, CourseEnrollment
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView
import bleach

@login_required
def courses(request):
    enrolled_courses = Course.objects.filter(courseenrollment__user=request.user)
    all_courses = Course.objects.all()
    return render(request, 'courses/courses.html', {'enrolled_courses': enrolled_courses, 'courses': all_courses})


class CourseDetailView(DetailView):
    model = Course
    template_name = 'courses/detail_view.html'
    context_object_name = 'course'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        course = self.get_object()
        if CourseEnrollment.objects.filter(user=user, course=course).exists():
            context['enrolled'] = True
        else:
            context['enrolled'] = False
        return context
    
    
def course_materials(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    materials = CourseMaterial.objects.filter(course=course) 
    
    cleaned_materials = []
    for material in materials:
        cleaned_content = bleach.clean(material.content, tags=['p', 'h3', 'strong','h1', 'h2', 'img'], attributes={'img': ['src']})
        material.content = cleaned_content
        cleaned_materials.append(material)
    return render(request, 'courses/course_materials.html', {'course': course, 'materials': cleaned_materials})


@login_required
def enroll_course(request, course_id):
    if request.method == 'POST':
        course = get_object_or_404(Course, pk=course_id)
        CourseEnrollment.objects.get_or_create(user=request.user, course=course)
        return redirect('course_detail', pk=course_id)
    