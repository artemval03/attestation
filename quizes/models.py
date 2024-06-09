# -*- coding: utf-8 -*-
from django.db import models
import random


DIFF_CHOICES = (
    ('легко', 'легко'),
    ('средне', 'средне'),
    ('сложно', 'сложно'),
)


class Quiz(models.Model):
    name = models.CharField(max_length=120, verbose_name='название')
    topic = models.CharField(max_length=120, verbose_name='описание')
    number_of_questions = models.IntegerField(verbose_name='количество вопросов')
    time = models.IntegerField(help_text="время на прохождение теста")
    required_score_to_pass = models.IntegerField( verbose_name='проходной балл')
    difficluty = models.CharField(max_length=6, choices=DIFF_CHOICES, verbose_name='сложность')

    def __str__(self):
        return f"{self.name}-{self.topic}"

    def get_questions(self):
        questions = list(self.question_set.all())
        random.shuffle(questions)
        return questions[:self.number_of_questions]

    class Meta:
        verbose_name = 'Тест'
        verbose_name_plural = 'Тесты'


class Teachers(models.Model):
    fio = models.CharField("ФИО", max_length=120)
    subject = models.CharField("Предмет", max_length=120)
    photo = models.ImageField(upload_to="teachers/%Y/%m/%d")

    def __str__(self):
        return self.fio


class VideoMaterials(models.Model):
    name = models.CharField('Название', max_length=255)
    link = models.TextField()

    def __str__(self):
        return self.name


class FileMaterials(models.Model):
    name = models.CharField('Название', max_length=255)
    description = models.TextField('Описание')
    file = models.FileField(upload_to='uploads/')

    def __str__(self):
        return self.name
