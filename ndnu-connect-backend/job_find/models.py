from django.db import models
from django.utils import timezone


class Job(models.Model):
    title = models.TextField(max_length=50, blank=True)
    description = models.TextField(max_length=250, blank=True)
    qualifications = models.TextField(max_length=250, blank=True)
    pay = models.TextField(max_length=115, blank=True)
    link = models.TextField(max_length=115, blank=True)
    date = models.DateTimeField(default=timezone.now)

    class JobTypes(models.TextChoices):
        FullTime = 'FULL', 'Full Time'
        PartTime = 'PART', 'Part Time'
        Intern = 'INTR', 'Internship'

    type = models.CharField(choices=JobTypes.choices, max_length=4, null=True)


    def __str__(self):
        return self.link

# Create your models here.
