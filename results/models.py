from django.db import models
from quizes.models import Quiz
from users.models import User

class Result(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.FloatField()

    def __str__(self):
        return str(str(self.user) + " " + str(self.quiz) + " " + str(self.score))

    class Meta:
        verbose_name = 'Результат'
        verbose_name_plural = 'Результаты'