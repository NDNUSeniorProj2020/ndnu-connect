<img src="https://github.com/NDNUSeniorProj2020/ndnu-connect/blob/master/ndnu-connect-backend/ndnuconnect/static/images/NDNU.png" width=750><br>
# NDNU Connect
NDNU Connect is a React-Django web application that allows past and present students of Notre Dame de Namur University (NDNU) to connect and help each other in their academic journeys and present career opportunities. These are achieved through the **Tutor**, **Job | Internship**, **Open Forum**, and **Alumni** applications.
### Why we made NDNU Connect
We made this app to help NDNU students connect with one another and serve as a medium for them to help each other through. We wanted to go beyond just serving current students because those of us working on this are soon-to-be alumni. By including an alumni aspect and a job page, the resources are open to all users so that users can connect with professionals who have graduated from NDNU.
## <img src="https://github.com/NDNUSeniorProj2020/ndnu-connect-client/blob/master/public/NDNU-Avatar-200x200.png" width=25> Applications
### Tutor
This application will match students and tutors with one another. Students and tutors will be able to create and view profiles that will display their schedules, subjects, locations, and prices. Students will also be able to rate their experience with tutor. Students and tutors will be able to find suitable tutors/students by searching for the ideal arrangement and being able to contact each other through their email addresses on their profiles.

**Tutor User Stories**
* [x] As a tutor, I would want to be able to see which students are looking for group tuition so that I can have them join my tuition group.
* [x] As a student, I want to be able to search for free tutors so that I can save money while learning.

### Job | Internship
This application allows users to post and view job opportunities. Users can post jobs that they can refer for, making this application much more effective at helping NDNU students and alumni find employment. Those searching for opportunities will be able to view the referrers' email to ask for help preparing for the prospect.

**Job | Internship User Stories**
* [x] As a new graduate, I want to be able to find job postings that have referrals so that I can at least get an interview instead of being rejected outright.

### Alumni
This application will allow past students to connect with each other by showing their graduation, year, and major.

**Alumni User Stories**
* [x] As an NDNU alumni, I want to be able to find other alumni so that I can catch up with old classmates.

### Open Forum
This application, as the name implies, is an open forum for users to share.

**Open Forum User Stories**
* [x] As an event organizer, I want to be able to create a post about an event so that other users can discuss and RSVP to that event.
* [ ] As someone with numerous posts, I want to be able to easily search through posts so that I can quickly read and respond to comments.

## Backend
This repository contains the backend for the project.

### Technologies Used
- <img src="https://github.com/NDNUSeniorProj2020/ndnu-connect/blob/master/ndnu-connect-backend/ndnuconnect/static/images/PythonDjango.png" width=25> **Django**
  - We chose Django for this project as the use of Python is growing and we are seeing more and more Django web applications, so this project would give us hands on experience with current technologies.
- <img src="https://github.com/NDNUSeniorProj2020/ndnu-connect/blob/master/ndnu-connect-backend/ndnuconnect/static/images/SQLite.png" width=25> **SQLite3**
  - We kept the default Django database for this project for simplicity.
- <img src="https://github.com/NDNUSeniorProj2020/ndnu-connect/blob/master/ndnu-connect-backend/ndnuconnect/static/images/AWS.png" width=25> **Amazon Web Services (AWS)**
  - We used AWS to deploy the back end as AWS is one of if not the most commonly used cloud service provider. It is another good experience for us.
  - Elastic Compute Cloud Instance (EC2)
    - Server to host the Django web application
  - Route 53
    - A domain name was required to certify the back end sever, allowing communications with the front end.
  - Load Balancer
    - The load balancing aspect of this Amazon application was not used, however it was required to obtain a free SSL certification from AWS.
- <img src="https://github.com/NDNUSeniorProj2020/ndnu-connect/blob/master/ndnu-connect-backend/ndnuconnect/static/images/WindowsServer.png" width=25> **Windows Server 2019**
  - While Windows isn't the front runner for deploying Django web applications, it was a good experience working with it and figuring out how everything is done this way.
  - Internet Information Services (IIS)
    - Chose IIS over Apache as IIS is faster than an Apache on Windows setup.
  - WFastCGI
    - The python package that allows Django to be deployed on IIS.

### Models
<img src="https://github.com/NDNUSeniorProj2020/ndnu-connect/blob/master/ndnu-connect-backend/ndnuconnect/static/images/DB%20Schema.png" width=750>

### Networking
|Model|RESTful API|
| ------------- | -------- |
|Alumni|https://praveenv.org/api/alumni/ |
|Board|https://praveenv.org/api/board/ |
|Department|https://praveenv.org/api/department/ |
|Job|https://praveenv.org/api/job/ |
|Post|https://praveenv.org/api/post/ |
|Schedule|https://praveenv.org/api/schedule/ |
|Student|https://praveenv.org/api/student/ |
|Subject|https://praveenv.org/api/subject/ |
|Topic|https://praveenv.org/api/topic/ |
|Tutor|https://praveenv.org/api/tutor/ |

## Setup
To get started with this project, you'll need to start in the `ndnu-connect`
directory in the `Terminal`, then go ahead and run the following commands:

`$ git checkout master`

`$ git pull`

`$ sudo pip3 install virtualenv`
* Run only when pulling from project for the 1st time

`$ virtualenv venv-ndnu-connect -p python3`
* Run only when pulling from project for the 1st time

`$ source venv-ndnu-connect/bin/activate`
* Enters the virtual environment

`$ pip3 install -r requirements.txt`
* Run only when in virtual environment

`$ cd ndnu-connect-backend`

`$ find . -path "*/migrations/*.py" -not -name "__init__.py" -delete`
* Deletes migration files

`$ find . -path "*/migrations/*.pyc"  -delete`
* Deletes migration files

`$ rm -rf db.sqlite3`
* Deletes preexisting db

`$ python manage.py makemigrations`

`$ python manage.py migrate`
* Recreates the db with new model changes

`$ python manage.py check`

`$ python Scripts/db_populate.py`
* Populates the db with sample data

`$ python manage.py runserver`

### Contributors:
* [Mark Falcone](https://github.com/markFalcone)
* [Matt Danielle](https://github.com/digitaluniverse)
* [Jonathon Chenvert](https://github.com/XZ7QN0)
* [Praveen Vandeyar](https://github.com/pv-gitjob)
* [Jose Alvarez Avina](https://github.com/jalvarez302)
* [Raul Flores](https://github.com/raulf21)
