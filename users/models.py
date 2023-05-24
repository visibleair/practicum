from django.db import models
from datetime import date
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    birth_date = models.DateField(verbose_name='Дата рождения', default=date.today)
    gender = models.CharField(max_length=10, choices=(('M', 'Мужской'), ('F', 'Женский')), verbose_name='Гендер')
    avatar = models.URLField(blank=True)
