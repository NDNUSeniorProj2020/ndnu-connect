# NDNU-Connect 

## Tutor Match
This application will match students and tutors with one another.

## Setup
To get started with this project, you'll need to start in the `ndnu-connect`
directory in the `Terminal`, then go ahead and run the following commands:

`$ git checkout master`

`$ git pull`

`$ sudo pip3 install virtualenv`

`$ virtualenv venv-ndnu-connect -p python3` <-- run once

`$ source venv-ndnu-connect/bin/activate` <-- Enters the virtual environment

`$ pip3 install -r requirements.txt` <-- Run only when in virtual environment

`$ cd ndnu-connect-backend`

`$ find . -path "*/migrations/*.py" -not -name "__init__.py" -delete`

`$ find . -path "*/migrations/*.pyc"  -delete` (deletes migration files)

`$ rm -rf db.sqlite3` (deletes existing db)

`$ python manage.py makemigrations`

`$ python manage.py migrate` (recreates the db)

`$ python manage.py check`

`$ python Scripts/db_populate.py` (populates db w/ data)

`$ python manage.py runserver`

### Contributors: 
* Mark Falcone
* Matt Danielle
* Jonathon Chenvert
* Praveen Vandeyar
* Leo Samuelson


