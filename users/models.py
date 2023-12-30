from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name='Почта')
    phone = models.CharField(max_length=25, verbose_name='Телефон', null=True, blank=True)
    country = models.CharField(max_length=255, verbose_name='Страна', null=True, blank=True)
    avatar = models.ImageField(upload_to='users/avatar', verbose_name='Аватар', null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
