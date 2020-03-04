import os
import sys

base_dir = os.getcwd()
sys.path.append(base_dir)

os.environ['DJANGO_SETTINGS_MODULE'] = 'ndnuconnect.settings'

import django
django.setup()

# User model
from accounts.models import Person
userCreate = Person()
user = userCreate.create_user('testUser', 'UserPassword')

# Tutor model
from tutor_match.models import Department, Subject, Tutor, Schedule
# Creates departments
addDepartment = Department(name='BUS')
addDepartment2 = Department(name='MTH')
addDepartment.save()
addDepartment2.save()

# Creates subjects
addSubject = Subject(subject='Business', semester='Spr2020', course_number='2215')
addSubject2 = Subject(subject='Algebra', semester='win2020', course_number='1234')
addSubject.save()
addSubject2.save()

# Creates a schedule
schedule1 = Schedule(monday="no",
                     tuesday="1-2",
                     wednesday="no",
                     thursday="3-4",
                     friday="5-6",
                     saturday="no",
                     sunday="no")
schedule1.save()

# Creates a tutor
addTutor = Tutor(pay=134.1,
                 subject=addSubject,
                 credentials="I have a degree",
                 method=1,
                 location=2,
                 description="im a nice person",
                 schedule=schedule1,
                 person=user)
addTutor.save()

# Creates a student
