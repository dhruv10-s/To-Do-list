from django.db import models

# Create your models here.
class student(models.Model):
    name = models.TextField()
    roll = models.IntegerField(default=0)