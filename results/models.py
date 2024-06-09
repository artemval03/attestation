from django.contrib.auth.models import User
from django.db import models
from quizes.models import Quiz


class Result(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, verbose_name='Тест')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    score = models.FloatField(verbose_name='Баллы')

    def __str__(self):
        return str(self.pk)

    class Meta:
        verbose_name = 'Результат'
        verbose_name_plural = 'Результаты'

