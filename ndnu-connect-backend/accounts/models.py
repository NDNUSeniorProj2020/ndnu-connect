from django.db import models
from django.contrib.auth.models import AbstractUser


class Person(AbstractUser):
    graduated = models.IntegerField(null=True)
    major = models.CharField(max_length=20, null=True)
    company = models.CharField(max_length=20, null=True)
    job_title = models.CharField(max_length=20, null=True)
    about = models.TextField(null=True)

    def __str__(self):
        return self.get_full_name()





