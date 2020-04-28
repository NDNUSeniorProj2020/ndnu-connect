from django.db import models


class Department(models.Model):
    class DepartmentNames(models.TextChoices):
        ACCOUNTING = 'ACC', 'Accounting'
        ART = 'ART', 'Art'
        ART_THERAPY = 'GPY', 'Art Therapy'
        BIOLOGY = 'BIO', 'Biology'
        BUSINESS_ADMINISTRATION = 'BUS', 'Business Administration'
        CHEMISTRY = 'CHE', 'Chemistry'
        CLINICAL_PSYCHOLOGY = 'CPY', 'Clinical Psychology'
        COMMUNICATION = 'COM', 'Communication'
        COMPUTER_SCIENCE = 'CSC', 'Computer Science'
        EDUCATION = 'EDU', 'Education'
        ENGLISH = 'ENG', 'English'
        ESL = 'TSL', 'English as a Second Language'
        HEALTH_SCIENCES = 'HSC', 'Health Sciences'
        HISTORY = 'HST', 'History'
        HUMAN_SERVICES = 'HSP', 'Human Services'
        KINESIOLOGY = 'KIN', 'Kinesiology'
        LIBERAL_STUDIES = 'LBS', 'Liberal Studies'
        MATHEMATICS = 'MTH', 'Mathematics'
        PHILOSOPHY = 'PHL', 'Philosophy'
        POLITICAL_SCIENCE = 'PSC', 'Political Science'
        PSYCHOLOGY = 'PSY', 'Psychology'
        RELIGIOUS_STUDIES = 'REL', 'Religious Studies'
        SOCIOLOGY = 'SOC', 'Sociology'
        SPANISH_STUDIES = 'SPA', 'Spanish Studies'

    name = models.CharField(choices=DepartmentNames.choices, max_length=3, null=True)

    def __str__(self):
        return "Department: " + self.name


class Subject(models.Model):
    subject = models.TextField(max_length=20, blank=True)
    semester = models.TextField(max_length=10, blank=True)
    course_number = models.TextField(max_length=10, blank=True)

    def get_subject_name(self):
        return self.subject

    def __str__(self):
        return self.subject


class SubjToDept(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return self.department.name + " - " + self.subject.subject


class Schedule(models.Model):
    monday = models.CharField(max_length=20, blank=True)
    tuesday = models.CharField(max_length=20, blank=True)
    wednesday = models.CharField(max_length=20, blank=True)
    thursday = models.CharField(max_length=20, blank=True)
    friday = models.CharField(max_length=20, blank=True)
    saturday = models.CharField(max_length=20, blank=True)
    sunday = models.CharField(max_length=20, blank=True)


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
    subject = models.ManyToManyField(Subject)
    credentials = models.TextField(max_length=50, blank=True)
    method = models.IntegerField(choices=TuitionMethod.choices, null=True)
    location = models.IntegerField(choices=TuitionLocation.choices, null=True)
    description = models.TextField(max_length=30, blank=True)
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE, null=True)
    rating = models.FloatField(null=True)
    num_of_ratings = models.FloatField(default=0)
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE, null=True)

    def save(self, *args, **kwargs):
        self.subject = self.subject.get_subject_name()
        super().save(*args, **kwargs)

    def get_subjects(self):
        return ",".join([str(p) for p in self.subject.all()])

    def __str__(self):
        return self.user.display_name + " - " + self.get_subjects()


class Student(models.Model):
    class YearInSchool(models.IntegerChoices):
        FRESHMAN = 1, 'Freshman'
        SOPHOMORE = 2, 'Sophomore'
        JUNIOR = 3, 'Junior'
        SENIOR = 4, 'Senior'
        GRADUATE = 5, 'Graduate'

    major = models.ForeignKey(Department, on_delete=models.CASCADE)
    pay = models.FloatField()
    subject = models.ManyToManyField(Subject)
    standing = models.IntegerField(choices=YearInSchool.choices, null=True)
    method = models.IntegerField(choices=TuitionMethod.choices, null=True)
    location = models.IntegerField(choices=TuitionLocation.choices, null=True)
    description = models.TextField(max_length=30, blank=True)
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE, null=True)

    def get_subjects(self):
        return ",".join([str(p) for p in self.subject.all()])

    def __str__(self):
        return self.user.display_name + " - Studying " + self.major.name
