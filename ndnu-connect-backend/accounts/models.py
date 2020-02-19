from django.db import models
from django.contrib.auth.models import User


class person(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    #alumni

    def __str__(self):
        return self.user.name




