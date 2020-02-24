import os, sys

sys.path.append('/Users/markfalcone/git/ndnu-connect/ndnu-connect-backend')

os.environ['DJANGO_SETTINGS_MODULE'] = 'ndnuconnect.settings'

import django
django.setup()

#  creating a user
# from accounts.models import person
# from django.contrib.auth.models import person
# testPerson=person.user.create_user('foo', password='testPassword123')
# testPerson.save()
# person1 = person.first_name ="andpioe"
# username = "scriptuser",person.user.password = "testPassword123" , person.user.first_name= 'first'





from tutor_match.models import Department, Subject, Tutor ,Schedule
# filling in the department
d = Department(name='BUS')
d2 = Department(name='MTH')
d.save()
d2.save()



# filing in the Subject
s = Subject(subject='Business', semester='Spr2020', course_number='2215')
s2 = Subject(subject='Algebra', semester='win2020', course_number='1234')
s.save()
s2.save()





#fill in the tutor
# t1 = Tutor(pay=134.1, subject=s, credentials="I have a degree",
# method=1, location= 2, description ="im a nice person", schedule =Schedule(monday = "12-2", tuesday = " r", wednesday="d", thursday="", friday="d", saturday="d", sunday="d"), rating=1,
# num_of_ratings=2, person= 'testPerson' )
# t1.save()
