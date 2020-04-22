from django.conf import settings
from django.db import models
from django.utils import timezone


class Work(models.Model):
    title = models.TextField()
    creator_name = models.TextField()
    thumbnail = models.ImageField()
    polled = models.IntegerField()
