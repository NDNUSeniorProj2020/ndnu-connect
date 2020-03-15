import os
import sys
import django

base_dir = os.getcwd()
sys.path.append(base_dir)
os.environ['DJANGO_SETTINGS_MODULE'] = 'ndnuconnect.settings'
django.setup()

# User model
from accounts.models import User, Person
# user, graduated, major, company, job_title, about
user1 = User.objects.create_user("JeffWorker@gmail.com", "workerpassword")
person1 = Person()
user2 = User.objects.create_user('JonTutor@gmail.com', 'tutorpassword')
person2 = Person()
user3 = User.objects.create_user('DoeStudent@student.com', 'studentsPassword')
person3 = Person()

jeff = person1.create(user1, 1990, "Art", "Google", "Graphic Designer", "I do art")
jon = person2.create(user2, 2021, "Business", "Self Employed", "Tutor", "I teach stuff")
doe = person3.create(user3, 2023, "Business", "", "", "")

# Tutor model
from tutor_match.models import Department, Subject, Tutor, Schedule, Student
# Creates departments
addDepartment = Department(name='BUS')
addDepartment2 = Department(name='MTH')
addDepartment3 = Department(name='ENG')
addDepartment.save()
addDepartment2.save()
addDepartment3.save()

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
schedule2 = Schedule(monday="1-4",
                     tuesday="1-2",
                     wednesday="1-2",
                     thursday="3-4",
                     friday="5-6",
                     saturday="1-9",
                     sunday="no")
schedule2.save()

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
                 description="Im a nice person",
                 schedule=schedule1,
                 person=jon)
addTutor.save()

# Creates a student
addStudent1 = Student(major=addDepartment,
                      pay="1.2",
                      standing=1,
                      method=1,
                      location=1,
                      description="Need help in BUS 101",
                      schedule=schedule2,
                      person=doe)
addStudent1.save()

# adds jobs
from job_find.models import Job

jobTest = Job(title="test1", description="description test", qualifications="bs degree", pay="1234", link="google.com",
              person=jeff, type='FULL')
jobTest.save()
