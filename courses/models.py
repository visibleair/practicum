from django.db import models
from datetime import date
from users.models import User

class Course(models.Model):
    name = models.CharField('Название курса', max_length=50)
    description = models.TextField('Описание курса')
    level = models.IntegerField('Сложность курса')
    date_create = models.DateField('Дата создания курса', default=date.today)
    date_lastchange = models.DateField('Дата последнего изменения курса', default=date.today)
    teacher = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Преподаватель',
        limit_choices_to={'groups__name': 'Преподаватель'}
    )
    
    def __str__(self):
        return self.name;
    
    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'
    
    @staticmethod
    def get_teacher_choices():
        return User.objects.filter(groups__name='Преподаватель')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['teacher'] = User.objects.get(id=context['course'].teacher_id)
        return context



class CourseMaterial(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    content = models.TextField()
    
    def __str__(self):
        return self.content;
    
    class Meta:
        verbose_name = 'Материал курса'
        verbose_name_plural = 'Материалы курса'
        
        

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

class ContentPriority(models.Model):
    number = models.IntegerField('Номер по порядку', unique=True)
    subtopic_number = models.IntegerField('Номер подтемы')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, verbose_name='Тип объекта')
    object_id = models.PositiveIntegerField('ID объекта')
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return f'Number: {self.number}, Subtopic Number: {self.subtopic_number}'

    class Meta:
        verbose_name = 'Очередность контента'
        verbose_name_plural = 'Очередность контента'
        ordering = ['number']


class Task(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    files_link = models.URLField()
    
    def __str__(self):
        return self.name;
    
    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'
        
        
class CourseEnrollment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrollment_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'course')
        

