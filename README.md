# NDNU-Connect 

## Tutor Match
This application will match students and tutors with one another.

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
