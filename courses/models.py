from django.db import models
from datetime import date
from users.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from quizes.models import Quiz


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
             
class Subtopics(models.Model):
    title = models.CharField('Название подтемы', max_length=50)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)        
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Название подтемы'
        verbose_name_plural = 'Название подтемы'

class PriorityContent(models.Model):
    number = models.AutoField('Номер по порядку', primary_key=True)
    subtopic_number = models.ForeignKey(Subtopics, on_delete=models.CASCADE)
    material_number = models.ForeignKey(CourseMaterial, on_delete=models.CASCADE, null=True, blank=True)
    task_number = models.ForeignKey(Task, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'Number: {self.number}, Subtopic Number: {self.subtopic_number}'

    class Meta:
        verbose_name = 'Очередность контента'
        verbose_name_plural = 'Очередность контента'
        ordering = ['number']
             
class CourseProgress(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    suptopic = models.ForeignKey(Subtopics, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'Course: {self.course.name}, Subtopic: {self.suptopic.title}'
    
    class Meta:
        verbose_name = 'Прогресс по курсу'
        verbose_name_plural = 'Прогресс по курсу'