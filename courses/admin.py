from django.contrib import admin
from .models import Course, CourseMaterial, Task, PriorityContent, Subtopics

admin.site.register(Course)
admin.site.register(Task)
admin.site.register(CourseMaterial)
admin.site.register(PriorityContent)
admin.site.register(Subtopics)