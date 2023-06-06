from django.shortcuts import render, get_object_or_404, redirect
from .models import Course, CourseMaterial, CourseEnrollment, Subtopics, PriorityContent, CourseProgress
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView
import bleach
from django.shortcuts import render, get_object_or_404

@login_required
def courses(request):
    enrolled_courses = Course.objects.filter(courseenrollment__user=request.user)
    all_courses = Course.objects.all()
    return render(request, 'courses/courses.html', {'enrolled_courses': enrolled_courses, 'courses': all_courses})


def courseDetailView(request, course_id):
    subtopics = Subtopics.objects.filter(course_id=course_id)
    course = get_object_or_404(Course, pk=course_id)
    user = request.user
    subtopic = get_object_or_404(CourseProgress, course_id=1, user_id=user.id).suptopic
   
     
    context = {
        'course': course,
        'subtopic': subtopic,
        'subtopics': subtopics
    }
    if CourseEnrollment.objects.filter(user=user, course=course).exists():
        context['enrolled'] = True
    else:
        context['enrolled'] = False
    
    
    return render(request, 'courses/detail_view.html', context)
    
    
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


def subtopic_detail_view(request, course_id, subtopic_id):
    subtopic = get_object_or_404(Subtopics, pk=subtopic_id, course=course_id)
    content = PriorityContent.objects.filter(subtopic_number=subtopic_id)
    course = get_object_or_404(Course, pk=course_id)
    course_progress, created = CourseProgress.objects.update_or_create(
        user=request.user,
        course=course,  # Присваиваем экземпляр модели Course
        defaults={'suptopic': subtopic}
    )
    if not created:
        # If the object already exists, update its attributes
        course_progress.course = course
        course_progress.suptopic = subtopic
        # Update any other attributes as needed
        course_progress.save()
    
    
    cleaned_contents = []
    for material in content:
        if material.material_number:
            cleaned_content = bleach.clean(material.material_number.content, tags=['p', 'h3', 'strong','h1', 'h2', 'img'], attributes={'img': ['src']})
            material.content = cleaned_content
            cleaned_contents.append(material)
        elif material.test_number:
            cleaned_contents.append(material)
    
    context = {
        'course': course,
        'subtopic': subtopic,
        'content': cleaned_contents,
    }
    return render(request, 'courses/course_materials.html', context)


    
