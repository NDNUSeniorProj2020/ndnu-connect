import os
import sys
import django

base_dir = os.getcwd()
sys.path.append(base_dir)
os.environ['DJANGO_SETTINGS_MODULE'] = 'ndnuconnect.settings'
django.setup()

# User model
from accounts.models import User
# Tutor model
from tutor_match.models import Department, Subject, Tutor, Schedule, Student
# Board model
from boards.models import Board, Topic, Post
# Job model
from job_find.models import Job

# Creating boards
try:
    board1 = Board(name='Announcements', description='Announce upcoming events at NDNU')
    board1.save()
    board2 = Board(name='Homework', description='Get help for homework.')
    board2.save()
    board3 = Board(name='Random', description='Random board')
    board3.save()

    print("The boards have been created.")
except:
    print("Boards exist")

# Creating a user and jobs
try:
    user1 = User.objects.create_user("JeffWorker@gmail.com", "workerpassword", first_name="John", last_name="Worker", graduated=True, year_graduated=2017, major="Computer Science", company="Google Inc.", job_title="Software Engineer")
    jobTest = Job(title="test1", description="description test", company="Google", location="Mountain View, CA",
                  qualifications="bs degree", pay="1234", link="google.com", user=user1, type='FULL')
    jobTest.save()

    print("A new user and their job has been added.")
except:
    print("User exists")

# Create a user, subject, schedule, and tutor
try:
    user2 = User.objects.create_user('JonTutor@gmail.com', 'tutorpassword', first_name='Jon', last_name='Tutor', graduated=True, year_graduated=2018, major='Biology')

    addSubject = Subject(subject='Business', semester='Spr2020', course_number='2215')
    addSubject.save()

    schedule1 = Schedule(monday="no",
                         tuesday="1-2",
                         wednesday="no",
                         thursday="3-4",
                         friday="5-6",
                         saturday="no",
                         sunday="no")
    schedule1.save()

    addTutor = Tutor(pay=134.1,
                     subject=addSubject,
                     credentials="I have a degree",
                     method=1,
                     location=2,
                     description="Im a nice person",
                     schedule=schedule1,
                     user=user2)
    addTutor.save()

    print("A new user and their subject, schedule, and tutor status has been added.")
except:
    print("User exists")

# Create a user, department, schedule, and student
try:
    user3 = User.objects.create_user('DoeStudent@student.com', 'studentsPassword')

    addDepartment = Department(name='BUS')
    addDepartment.save()

    schedule2 = Schedule(monday="1-4",
                         tuesday="1-2",
                         wednesday="1-2",
                         thursday="3-4",
                         friday="5-6",
                         saturday="1-9",
                         sunday="no")
    schedule2.save()

    addStudent1 = Student(major=addDepartment,
                          pay="1.2",
                          standing=1,
                          method=1,
                          location=1,
                          description="Need help in BUS 101",
                          schedule=schedule2,
                          user=user3)
    addStudent1.save()

    print("A new user and their schedule and student help status has been added.")
except:
    print("User exists")

# Create four users
try:
    user4 = User.objects.create_user('john@mynametoo.com', 'blackcherry500', first_name='John', last_name='Cherry', graduated=True, year_graduated=2010, major='Business Administration', company='KPMG', job_title='Financial Advisor')
    user5 = User.objects.create_user('jacob@mynametoo.com', 'raspberry500', first_name='Jacob', last_name='Raspberry')
    user6 = User.objects.create_user('jingleheimer@mynametoo.com', 'applehoney500', first_name='Jingle', last_name='Heimer')
    user7 = User.objects.create_user('schmidt@mynametoo.com', 'peach500', first_name='Nicholas', last_name='Schmidt', graduated=True, year_graduated=2005, major='Accounting & Finance', company='Facebook Inc.', job_title='Accountant')
    print("The 4 users have been created.")
except:
    print("The 4 users already exist")

# Create departments
try:
    addDepartment2 = Department(name='MTH')
    addDepartment2.save()
    addDepartment3 = Department(name='ENG')
    addDepartment3.save()

    print("2 new departments have been added.")
except:
    print("Departments exist")

# Create a subject
try:
    addSubject2 = Subject(subject='Algebra', semester='win2020', course_number='1234')
    addSubject2.save()

    print("A new subject has been added.")
except:
    print("Subject exists")

# Creates topics and posts
try:
    topic1 = Topic(subject='Math', board=board2, starter=user2)
    topic1.save()
    topic2 = Topic(subject='Computer Science', board=board2, starter=user3)
    topic2.save()
    topic3 = Topic(subject='Athletics', board=board1, starter=user1)
    topic3.save()
    post1 = Post(message='Need help with problem', topic=topic1, created_by=user1)
    post1.save()
    post2 = Post(message='Basketball game Saturday', topic=topic3, created_by=user2)
    post2.save()

    print("3 new topics and 2 new posts have been added.")
except:
    print("These topics and/or posts already exist.")
