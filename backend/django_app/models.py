from django.db import models
from django.contrib.auth.models import User

class News(models.Model):
    name = models.CharField(max_length=20)
    title = models.CharField(max_length=300)
    news = models.CharField(max_length=800)

    def __str__(self):
        return self.title

class Complaint(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=800)

    def __str__(self):
        return self.description

