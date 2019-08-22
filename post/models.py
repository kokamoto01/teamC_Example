from django.db import models

# Create your models here.
from django.db import models

from register.models import User


class Post(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=200, default='')
    content_path = models.CharField(max_length=1000)
    thumbnail_path = models.CharField(max_length=1000)
    user = models.ForeignKey(User, blank=False, verbose_name='ユーザ', on_delete=models.CASCADE)
