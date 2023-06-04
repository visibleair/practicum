from django.db import models
from users.models import User
class Test(models.Model):
    title = models.CharField('Название теста', max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тест'
        verbose_name_plural = 'Тесты'


class Question(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name='questions')
    question_text = models.CharField('Текст вопроса', max_length=200)
    correct_answer = models.CharField('Правильный ответ', max_length=100)

    def __str__(self):
        return self.question_text

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    answer_text = models.CharField('Текст варианта ответа', max_length=100)

    def __str__(self):
        return self.answer_text

    class Meta:
        verbose_name = 'Вариант ответа'
        verbose_name_plural = 'Варианты ответов'


class UserAnswer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    chosen_answer = models.CharField('Ответ пользователя', max_length=50)
    is_correct = models.BooleanField('Правильный ответ', default=False)

    def __str__(self):
        return self.question.question_text + " - " + self.chosen_answer + " " + self.user.username
    
    class Meta:
        verbose_name = 'Ответ пользователя'
        verbose_name_plural = 'Ответы пользователей'