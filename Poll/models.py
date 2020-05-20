from django.conf import settings
from django.db import models
from django.utils import timezone


class Work(models.Model):
    title = models.TextField()
    creator_name = models.TextField()
    thumbnail = models.ImageField(upload_to="gallery")
    polled = models.IntegerField()

    def __str__(self):
        return self.title