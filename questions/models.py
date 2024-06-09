# -*- coding: utf-8 -*-
from django.db import models
from quizes.models import Quiz


class Question(models.Model):
    text = models.CharField(max_length=200, verbose_name='Вопрос')
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, verbose_name='Тест')
    created = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')

    def __str__(self):
        return str(self.text)

    def get_answers(self):
        return self.answer_set.all()

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


class Answer(models.Model):
    text = models.CharField(max_length=200, verbose_name='Ответ')
    correct = models.BooleanField(default=False, verbose_name='Верно или нет')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='Вопрос')
    created = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')

    def __str__(self):
        return f"Вопрос: {self.question.text}, ответ: {self.text}, Верно или нет: {self.correct}"

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'
