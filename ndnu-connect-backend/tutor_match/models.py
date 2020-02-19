from django.db import models


class Department(models.Model):

    class DepartmentNames(models.TextChoices):
        ACCOUNTING = 'ACC', 'Accounting'
        BUSINESS_ADMINISTRATION = 'BUS', 'Business Administration'
        #More, maybe with BA, BS, MA, MS declarations

    name = models.CharField(choices=DepartmentNames.choices, max_length=3, null=True)

    def __str__(self):
        return self.name


class Subject(models.Model):
    subject = models.TextField(max_length=20, blank=True)
    semester = models.TextField(max_length=10, blank=True)
    course_number = models.TextField(max_length=10, blank=True)
    #notes

    def __str__(self):
        return self.subject


class SubjToDept(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return self.department + " " + self.subject


class Schedule(models.Model):
    monday = models.TextField(max_length=30, blank=True)
    tuesday = models.TextField(max_length=30, blank=True)
    wednesday = models.TextField(max_length=30, blank=True)
    thursday = models.TextField(max_length=30, blank=True)
    friday = models.TextField(max_length=30, blank=True)
    saturday = models.TextField(max_length=30, blank=True)
    sunday = models.TextField(max_length=30, blank=True)


class TuitionMethod(models.IntegerChoices):
    PRIVATE = 1, 'Private'
    GROUP = 2, 'Group'
    EITHER = 3, 'Either'


class TuitionLocation(models.IntegerChoices):
    SCHOOL = 1, 'School'
    ANYWHERE = 2, 'Anywhere'
    OTHER = 3, 'Other'


class Tutor(models.Model):

    pay = models.FloatField()
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, null=True)
    credentials = models.TextField(max_length=50, blank=True)
    method = models.IntegerField(choices=TuitionMethod.choices, null=True)
    location = models.IntegerField(choices=TuitionLocation.choices, null=True)
    description = models.TextField(max_length=30, blank=True)
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE, null=True)
    rating = models.FloatField(null=True)
    num_of_ratings = models.FloatField(default=0)
    person = models.ForeignKey('accounts.person', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.subject + " " + self.pay


class Student(models.Model):

    class YearInSchool(models.IntegerChoices):
        FRESHMAN = 1, 'Freshman'
        SOPHOMORE = 2, 'Sophomore'
        JUNIOR = 3, 'Junior'
        SENIOR = 4, 'Senior'
        GRADUATE = 5, 'Graduate'

    major = models.ForeignKey(Department, on_delete=models.CASCADE)
    pay = models.FloatField()
    standing = models.IntegerField(choices=YearInSchool.choices, null=True)
    method = models.IntegerField(choices=TuitionMethod.choices, null=True)
    location = models.IntegerField(choices=TuitionLocation.choices, null=True)
    description = models.TextField(max_length=30, blank=True)
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE, null=True)
    person = models.ForeignKey('accounts.person', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.major + " " + self.pay
