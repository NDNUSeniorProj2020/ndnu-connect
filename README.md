# NDNU Connect
NDNU Connect is a React-Django web application that allows past and present students of Notre Dame de Namur University (NDNU) to connect and help each other in their academic journeys and present career opportunities. These are achieved through the Tutor, Job | Internship, and Alumni applications.
### Tutor
This application will match students and tutors with one another. Students and tutors will be able to create and view profiles that will display their schedules, subjects, locations, and prices. Students will also be able view each tutor's rating that they can vote on. Students and tutors will be able to find suitable tuition by searching for the ideal arrangement and contact each other through their email addresses on their profiles.
### Job | Internship
This application allows users to post and view job opportunities. Users can post jobs that they can refer for, making this application much more effective at helping NDNU students and alumni find employment. Those searching for opportunities will be able to view the referrers email to ask for help preparing for the prospect.
### Alumni
This application will allow past students to connect with each other by showing their graduation year and major.
### Open Forum
This application, as the name suggests, is an open forum for users to organize events or discuss any issues related to NDNU.
## Back End
This repository contains the back end for the project.
- Django
  - We chose Django for this project as the use of Python is growing and we are seeing more and more Django web applications, so this project would give us hands on experience with current technologies.
- SQLite3
  - We kept the default Django database for this project for simplicity.
- Amazon Web Services (AWS)
  - We used AWS to deploy the back end as AWS is one of if not the most commonly used cloud service provider. It is another good experience for us.
  - Elastic Compute Cloud Instance, Windows Server 2019
    - While Windows isn't the front runner for deploying Django web applications, it was a good experience working with it and figuring out how everything is done this way.
  - Route 53
    - A domain name was required to certify the back end sever, allowing communications with the front end.
  - Load Balancer
    - The load balancing aspect of this Amazon application was not used, however it was required to obtain a free SSL certification from AWS.

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
* Mark Falcone
* Matt Danielle
* Jonathon Chenvert
* Praveen Vandeyar
* Leo Samuelson
* Jose Alvarez Avina
* Ervin Elias
* Raul Flores
