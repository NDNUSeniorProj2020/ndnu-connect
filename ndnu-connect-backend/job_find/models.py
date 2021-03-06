from django.db import models
from django.utils import timezone


class Job(models.Model):
    title = models.CharField(max_length=100, blank=True)
    company = models.CharField(max_length=100, blank=True)
    location = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    qualifications = models.TextField(blank=True)
    pay = models.CharField(max_length=50, blank=True)
    link = models.URLField(max_length=500, blank=True)
    date = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE, null=True)

    class JobTypes(models.TextChoices):
        FullTime = 'FULL', 'Full Time'
        PartTime = 'PART', 'Part Time'
        Intern = 'INTR', 'Internship'

    type = models.CharField(choices=JobTypes.choices, max_length=4, null=True)

    def __str__(self):
        return "Job Posting: " + self.title
