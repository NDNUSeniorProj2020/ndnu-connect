from django.db import models
from django.utils import timezone


class Job(models.Model):
    title = models.TextField(max_length=50, blank=true)
    description = models.TextField(max_length=250, blank=true)
    qualifications = models.TextField(max_length=250, blank=true)

    class JobTypes(models.TextChoices):
        FullTime = 'FULL', 'Full Time'
        PartTime = 'PART', 'Part Time'
        Intern = 'INTR', 'Internship'

        def __str__(self):

    return self.pay

    type = models.CharField(choices=JobTypes.choices, max_length=4, null=True)
    pay = models.TextField(max_length=115, blank=true)
    link = models.TextField(max_length=115, blank=true)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.link

# Create your models here.
