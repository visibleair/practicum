from django.contrib import admin
from .models import UserAnswer, Answer, Question, Test

admin.site.register(UserAnswer)
admin.site.register(Answer)
admin.site.register(Question)
admin.site.register(Test)
