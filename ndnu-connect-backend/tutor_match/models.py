from django.db import models


class Schedule(models.Model):
    monday = models.TextField(max_length=30, blank=True)
    tuesday = models.TextField(max_length=30, blank=True)
    wednesday = models.TextField(max_length=30, blank=True)
    thursday = models.TextField(max_length=30, blank=True)
    friday = models.TextField(max_length=30, blank=True)
    saturday = models.TextField(max_length=30, blank=True)
    sunday = models.TextField(max_length=30, blank=True)


class Tutor(models.Model):

    class TuitionMethod(models.IntegerChoices):
        PRIVATE = 1, 'Private'
        GROUP = 2, 'Group'
        EITHER = 3, 'Either'

    class TuitionLocation(models.IntegerChoices):
        SCHOOL = 1, 'School'
        ANYWHERE = 2, 'Anywhere'
        OTHER = 3, 'other'

    pay = models.FloatField()
    subject = models.TextField(max_length=50, blank=True)
    credentials = models.TextField(max_length=50, blank=True)
    method = models.IntegerField(choices=TuitionMethod.choices, null=True)
    location = models.IntegerField(choices=TuitionLocation.choices, null=True)
    description = models.TextField(max_length=30, blank=True)
    schedule = models.OneToOneField(Schedule, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.subject


class Student(models.Model):

    class YearInSchool(models.IntegerChoices):
        FRESHMAN = 1, 'Freshman'
        SOPHOMORE = 2, 'Sophomore'
        JUNIOR = 3, 'Junior'
        SENIOR = 4, 'Senior'
        GRADUATE = 5, 'Graduate'

    class TuitionMethod(models.IntegerChoices):
        PRIVATE = 1, 'Private'
        GROUP = 2, 'Group'
        EITHER = 3, 'Either'

    class TuitionLocation(models.TextChoices):
        SCHOOL = 1, 'School'
        ANYWHERE = 2, 'Anywhere'
        OTHER = 3, 'other'

    major = models.TextField(max_length=30, blank=True)
    pay = models.FloatField()
    standing = models.IntegerField(choices=YearInSchool.choices, null=True)
    method = models.IntegerField(choices=TuitionMethod.choices, null=True)
    location = models.IntegerField(choices=TuitionLocation.choices, null=True)
    description = models.TextField(max_length=30, blank=True)
    schedule = models.OneToOneField(Schedule, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.major
