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
user1 = User.objects.create_user("JeffWorker@gmail.com", "workerpassword", "jeffworker")
person1 = Person()
user2 = User.objects.create_user('JonTutor@gmail.com', 'tutorpassword', 'jontutor')
person2 = Person()
user3 = User.objects.create_user('DoeStudent@student.com', 'studentsPassword', 'doestudent')
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
                 user=user2)
addTutor.save()

# Creates a student
addStudent1 = Student(major=addDepartment,
                      pay="1.2",
                      standing=1,
                      method=1,
                      location=1,
                      description="Need help in BUS 101",
                      schedule=schedule2,
                      user=user3)
addStudent1.save()

# adds jobs
from job_find.models import Job

jobTest = Job(title="test1", description="description test", qualifications="bs degree", pay="1234", link="google.com",
              user=user1, type='FULL')
jobTest.save()

from boards.models import Board, Topic, Post

# Create boards
board1 = Board(name='Announcements', description='Announce upcoming events at NDNU')
board1.save()
board2 = Board(name='Homework', description='Get help for homework.')
board2.save()
board3 = Board(name='Random', description='Random board')
board3.save()

# Create topics
topic1 = Topic(subject='Math', board=board2, starter=user2)
topic1.save()
topic2 = Topic(subject='Computer Science', board=board2, starter=user3)
topic2.save()
topic3 = Topic(subject='Athletics', board=board1, starter=user1)
topic3.save()

# Create posts
post1 = Post(message='Need help with problem', topic=topic1, created_by=user1)
post1.save()
post2 = Post(message='Basketball game Saturday', topic=topic3, created_by=user2)
post2.save()
