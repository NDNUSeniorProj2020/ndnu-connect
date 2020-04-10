import os
import sys
import django

base_dir = os.getcwd()
sys.path.append(base_dir)
os.environ['DJANGO_SETTINGS_MODULE'] = 'ndnuconnect.settings'
django.setup()

# User model
from accounts.models import User, Person
# Tutor model
from tutor_match.models import Department, Subject, Tutor, Schedule, Student
# Board model
from boards.models import Board, Topic, Post
# Job model
from job_find.models import Job

try:
    # Create boards
    board1 = Board(name='Announcements', description='Announce upcoming events at NDNU')
    board1.save()
    board2 = Board(name='Homework', description='Get help for homework.')
    board2.save()
    board3 = Board(name='Random', description='Random board')
    board3.save()
except:
    print("Boards exist")

try:
    user1 = User.objects.create_user("JeffWorker@gmail.com", "workerpassword")
    person1 = Person()
    jeff = person1.create(user1, 1990, "Art", "Google", "Graphic Designer", "I do art")
    # adds jobs
    jobTest = Job(title="test1", description="description test", qualifications="bs degree", pay="1234",
                  link="google.com",
                  user=user1, type='FULL')
    jobTest.save()

except:
    print("User exists")
try:
    user2 = User.objects.create_user('JonTutor@gmail.com', 'tutorpassword')
    person2 = Person()
    jon = person2.create(user2, 2021, "Business", "Self Employed", "Tutor", "I teach stuff")
    # Creates subject
    addSubject = Subject(subject='Business', semester='Spr2020', course_number='2215')
    addSubject.save()
    # Creates schedule
    schedule1 = Schedule(monday="no",
                         tuesday="1-2",
                         wednesday="no",
                         thursday="3-4",
                         friday="5-6",
                         saturday="no",
                         sunday="no")
    schedule1.save()
    # Creates tutor
    addTutor = Tutor(pay=134.1,
                     subject=addSubject,
                     credentials="I have a degree",
                     method=1,
                     location=2,
                     description="Im a nice person",
                     schedule=schedule1,
                     user=user2)
    addTutor.save()
except:
    print("User exists")
try:
    user3 = User.objects.create_user('DoeStudent@student.com', 'studentsPassword')
    person3 = Person()
    doe = person3.create(user3, 2023, "Business", "", "", "")
    # Creates department
    addDepartment = Department(name='BUS')
    addDepartment.save()
    # Creates schedule
    schedule2 = Schedule(monday="1-4",
                         tuesday="1-2",
                         wednesday="1-2",
                         thursday="3-4",
                         friday="5-6",
                         saturday="1-9",
                         sunday="no")
    schedule2.save()
    # Creates student
    addStudent1 = Student(major=addDepartment,
                          pay="1.2",
                          standing=1,
                          method=1,
                          location=1,
                          description="Need help in BUS 101",
                          schedule=schedule2,
                          user=user3)
    addStudent1.save()
except:
    print("User exists")

try:
    addDepartment2 = Department(name='MTH')
    addDepartment2.save()
    addDepartment3 = Department(name='ENG')
    addDepartment3.save()
except:
    print("Departments exist")

try:
    addSubject2 = Subject(subject='Algebra', semester='win2020', course_number='1234')
    addSubject2.save()
except:
    print("Subjects exist")

try:
    # Create topic
    topic1 = Topic(subject='Math', board=board2, starter=user2)
    topic1.save()
    topic2 = Topic(subject='Computer Science', board=board2, starter=user3)
    topic2.save()
    topic3 = Topic(subject='Athletics', board=board1, starter=user1)
    topic3.save()
    # Create post
    post1 = Post(message='Need help with problem', topic=topic1, created_by=user1)
    post1.save()
    post2 = Post(message='Basketball game Saturday', topic=topic3, created_by=user2)
    post2.save()
except:
    print("Something doesn't exist, or already exists")
