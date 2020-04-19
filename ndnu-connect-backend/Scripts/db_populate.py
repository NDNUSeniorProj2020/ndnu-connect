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
    user1 = User.objects.create_user("JeffWorker@gmail.com", "workerpassword")
    person1 = Person()
    jeff = person1.create(user1, False, 1990, "Art", "Google", "Graphic Designer", "I make graphic designs.")

    jobTest = Job(title="test1", description="description test", company="Google", location="Mountain View, CA",
                  qualifications="bs degree", pay="1234", link="google.com", user=user1, type='FULL')
    jobTest.save()

    print("A new user and their job has been added.")
except:
    print("User exists")

# Create a user, subject, schedule, and tutor
try:
    user2 = User.objects.create_user('JonTutor@gmail.com', 'tutorpassword')
    person2 = Person()
    jon = person2.create(user2, True, 2021, "Business", "Self Employed", "Tutor", "I teach stuff")

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
    person3 = Person()
    doe = person3.create(user3, True, 2023, "Business", "N/A", "Student", "I'm a student that needs help in class.")

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
    user4 = User.objects.create_user('john@mynametoo.com', 'blackcherry500')
    person4 = Person()
    john = person4.create(user4, True, 2018, "Computer Science", "Four Brothers: Criminal Justice",
                         "Software Engineer",
                         "I develop software for my company, founded with my four brothers.")

    user5 = User.objects.create_user('jacob@mynametoo.com', 'raspberry500')
    person5 = Person()
    jacob = person5.create(user5, False, 2023, "Criminal Justice", "Four Brothers: Criminal Justice",
                          "Detective",
                          "I investigate criminal activities for a company with my four brothers.")

    user6 = User.objects.create_user('jingleheimer@mynametoo.com', 'applehoney500')
    person6 = Person()
    jingleheimer = person6.create(user6, True, 2018, "Biology", "Four Brothers: Criminal Justice",
                                 "Forensic Scientist",
                                 "I analyze biological patterns and clues in a company with my four brothers.")

    user7 = User.objects.create_user('schmidt@mynametoo.com', 'peach500')
    person7 = Person()
    schmidt = person7.create(user7, False, 2023, "English", "Four Brothers: Criminal Justice",
                            "Administrator",
                            "I write reports to send out in a company with my four brothers.")
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
