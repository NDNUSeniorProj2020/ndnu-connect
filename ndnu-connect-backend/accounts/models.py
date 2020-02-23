from django.db import models
from django.contrib.auth.models import AbstractUser


class Person(AbstractUser):
    graduated = models.IntegerField(null=True, blank=True)
    major = models.CharField(max_length=20, null=True, blank=True)
    company = models.CharField(max_length=20, null=True, blank=True)
    job_title = models.CharField(max_length=20, null=True, blank=True)
    about = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.username





