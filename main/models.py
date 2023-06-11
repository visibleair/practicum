from django.db import models

class News(models.Model):
    title = models.CharField('Заголовок', max_length=50)
    content = models.TextField('Содержимое новости', max_length=250)
    date = models.DateTimeField('Дата новости')