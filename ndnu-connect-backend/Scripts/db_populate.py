import os, sys

#sys.path.append('/Users/markfalcon/git/ndnu-connect/ndnu-connect-backend')

base_dir = os.getcwd()

sys.path.append(base_dir)

os.environ['DJANGO_SETTINGS_MODULE'] = 'ndnuconnect.settings'

import django
django.setup()

#  creating a user
from accounts.models import Person
userCreate = Person()
user = userCreate.create_user('testUser', 'UserPassword')




from tutor_match.models import Department, Subject, Tutor ,Schedule
# filling in the department
addDepartment = Department(name='BUS')
addDepartment2 = Department(name='MTH')
addDepartment.save()
addDepartment2.save()



# filing in the Subject
addSubject = Subject(subject='Business', semester='Spr2020', course_number='2215')
addSubject2 = Subject(subject='Algebra', semester='win2020', course_number='1234')
addSubject.save()
addSubject2.save()


scedule1 = Schedule(monday="no", tuesday="1-2", wednesday="no", thursday="3-4",
friday="5-6", saturday="no", sunday="no")
scedule1.save()

#fill in the tutor
addTutor = Tutor(pay=134.1, subject=addSubject, credentials="I have a degree",
method=1, location= 2, description ="im a nice person", schedule = scedule1, person = user)
addTutor.save()
