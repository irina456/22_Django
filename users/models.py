from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, verbose_name='email')
    avatar = models.ImageField(upload_to="avatars/", verbose_name='Аватар', blank=True, null=True)
    phone_number = models.CharField(max_length=50, verbose_name='Номер телефона')
    country = models.CharField(max_length=50, verbose_name='Страна')
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        return self.email