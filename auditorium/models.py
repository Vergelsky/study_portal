from django.db import models
from users.models import NULLABLE

class Course(models.Model):
    name = models.CharField(max_length=120, verbose_name='Название')
    description = models.CharField(max_length=600, verbose_name='Описание')
    image = models.ImageField(upload_to='images/', verbose_name='Превью', **NULLABLE)

    def __str__(self):
        return self.name

class Lesson(models.Model):
    name = models.CharField(max_length=120, verbose_name='Название')
    description = models.CharField(max_length=600, verbose_name='Описание')
    image = models.ImageField(upload_to='images/', verbose_name='Превью', **NULLABLE)
    video = models.URLField(verbose_name='Видео', **NULLABLE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Курс')

    def __str__(self):
        return self.name
