# Time tracking web service

Test task. Simple time tracking web service for tracking your work hours across projects.
You can find full test task description (in Russian) [here](test_task.pdf).

## How to install

#### Requirements (see Pipfile for details):
- python 3.6
- django 2.2

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
#### Run the server:
```sh
python manage.py runserver 
```
## Testing
```sh
 python manage.py test
```
