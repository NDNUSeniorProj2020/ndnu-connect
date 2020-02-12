from django.db import models


class Tutor(models.Model):
    name = models.TextField(max_length=100)
    charges = models.BooleanField()
    charge_fee = models.FloatField()
    subject = models.TextField(max_length=60)

    def __str__(self):
        return self.name
