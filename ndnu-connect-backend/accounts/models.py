from django.db import models
from django.contrib.auth.models import User


class Alumni(models.Model):
    graduated = models.IntegerField(null=True)
    major = models.CharField(max_length=20)
    company = models.CharField(max_length=20)
    job_title = models.CharField(max_length=20)
    about = models.TextField(null=True)


class Person(models.Model):
    user = models.ForeignKey(User, unique=True, null=True, on_delete=models.CASCADE)
    alumni = models.ForeignKey(Alumni, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.name





