from django.db import models


class Person(models.Model):
    person_name = models.CharField(max_length=30, null=True)
    username = models.CharField(max_length=20, null=True)
    email = models.EmailField(max_length=30, null=True)
    password = models.CharField(max_length=30, null=True)
    graduated = models.IntegerField(null=True)
    major = models.CharField(max_length=20, null=True)
    company = models.CharField(max_length=20, null=True)
    job_title = models.CharField(max_length=20, null=True)
    about = models.TextField(null=True)

    def __str__(self):
        return self.person_name





