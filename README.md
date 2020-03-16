# Time tracking web service

## How to install
Create virtual environment and install dependencies with [pipenv](https://github.com/pypa/pipenv):
```sh
pipenv install
```
Apply migrations and create a user:
```sh
cd time_tracker_project
python manage.py migrate
python manage.py createsuperuser
```
Run the server:
```sh
python manage.py runserver 
```
