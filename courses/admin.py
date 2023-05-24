from django.contrib import admin
from .models import Course, CourseMaterial, Task, ContentPriority

admin.site.register(Course)
admin.site.register(Task)
admin.site.register(CourseMaterial)
admin.site.register(ContentPriority)