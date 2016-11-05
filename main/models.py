from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Messages(models.Model):
    content = models.CharField(max_length=100)
    userId = models.IntegerField()

    def __str__(self):
        return self.content
