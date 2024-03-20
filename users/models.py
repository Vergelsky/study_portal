from django.contrib.auth.models import AbstractUser
from django.db import models

from django.utils.translation import gettext_lazy as _


NULLABLE = {'blank': True, 'null': True }

# Create your models here.
class User(AbstractUser):
    username = None
    email = models.EmailField(_("email address"), unique=True)

    phone = models.CharField(max_length=35, verbose_name='телефон', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)
    city = models.CharField(max_length=70, verbose_name='страна', **NULLABLE)


    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []


