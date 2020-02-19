from django.db import models

class person(models.Model):

    person_name = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.name
