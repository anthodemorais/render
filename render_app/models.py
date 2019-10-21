from django.db import models
from django import forms
from django.contrib.auth.models import User

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=200)
    course = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField()
    deadline = models.DateTimeField()
    team = models.BooleanField(default=False)
    user_ids = models.ManyToManyField(User)
    done_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=200)
    years = models.IntegerField(default=1)
    teacher_name = models.CharField(max_length=100, default='')
    teacher_email = models.EmailField(max_length=264, default='')