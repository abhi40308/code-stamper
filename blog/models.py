from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='media', default='no-img.png')
    text = models.TextField()
    published_date = models.DateTimeField(
            default=timezone.now)
    section = models.CharField(max_length=15, default='home')

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title