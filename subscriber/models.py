from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from project.models import Project


class Subscriber(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
