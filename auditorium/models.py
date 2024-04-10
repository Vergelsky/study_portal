from django.db import models
from users.models import NULLABLE, User


class Course(models.Model):
    name = models.CharField(max_length=120, verbose_name='Название')
    description = models.CharField(max_length=600, verbose_name='Описание')
    image = models.ImageField(upload_to='images/', verbose_name='Превью', **NULLABLE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор', **NULLABLE)
    price = models.IntegerField(verbose_name='Цена', **NULLABLE)

    def __str__(self):
        return self.name


class Lesson(models.Model):
    name = models.CharField(max_length=120, verbose_name='Название')
    description = models.CharField(max_length=600, verbose_name='Описание')
    image = models.ImageField(upload_to='images/', verbose_name='Превью', **NULLABLE)
    video = models.URLField(verbose_name='Видео', **NULLABLE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Курс', **NULLABLE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор', **NULLABLE)
    price = models.IntegerField(verbose_name='Цена', **NULLABLE)

    def __str__(self):
        return self.name


class Payments(models.Model):
    PAYMENT_METHODS = (
        ('cash', 'Cash'),
        ('card', 'Card')
    )
    user = models.ForeignKey(User, models.CASCADE, verbose_name='пользователь')
    date = models.DateTimeField(auto_now=True, verbose_name='дата оплаты')
    course = models.ForeignKey(Course, models.CASCADE, verbose_name='оплаченный курс', **NULLABLE)
    lesson = models.ForeignKey(Lesson, models.CASCADE, verbose_name='оплаченный урок', **NULLABLE)
    amount = models.FloatField(default=0, verbose_name='сумма оплаты')
    field = models.TextField(choices=PAYMENT_METHODS, verbose_name='способ оплаты')
    stripe_link = models.URLField(max_length=600, verbose_name='Ссылка на оплату', **NULLABLE)


class Subscribe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Подписчик')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='курс')
