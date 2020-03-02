from django.db import models
from django.utils import timezone


class Job(models.Model):
    title = models.CharField(max_length=50, blank=True)
    description = models.TextField(max_length=300, blank=True)
    qualifications = models.TextField(max_length=250, blank=True)
    pay = models.CharField(max_length=50, blank=True)
    link = models.URLField(max_length=115, blank=True)
    date = models.DateTimeField(default=timezone.now)
    person = models.ForeignKey('accounts.Person', on_delete=models.CASCADE, null=True)  # Referrer

    class JobTypes(models.TextChoices):
        FullTime = 'FULL', 'Full Time'
        PartTime = 'PART', 'Part Time'
        Intern = 'INTR', 'Internship'

    type = models.CharField(choices=JobTypes.choices, max_length=4, null=True)

    def __str__(self):
        return self.link
