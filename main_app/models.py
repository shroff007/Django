from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Person(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length = 100)
    userType = models.CharField(max_length = 100)

    def __str__(self):
        return self.name
