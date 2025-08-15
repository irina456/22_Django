from django.db import models
from django.core.mail import send_mail
from django.conf import settings
from dotenv import load_dotenv
import os

load_dotenv()

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    preview = models.ImageField(upload_to="images/blog/%Y/%m/%d")
    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)
    views = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = verbose_name
        ordering = ['created_at']

    def __str__(self):
        post_str = f'''{self.title}
{self.content}
Создано: {self.created_at}, Опубликовано: {self.is_published}, Просмотров: {self.views}'''
        return post_str

    def send_congratulation_email(self):
        subject = f'Поздравление: статья "{self.title}" достигла 100 просмотров!'
        message = f'Статья "{self.title}" (ID: {self.id}) достигла {self.views} просмотров!'
        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [os.getenv('RECIPIENT_EMAIL')],
            fail_silently=False,
        )

