# Library-Management-System
This is the basic library management system that is written with django class based function . The main goal of this system was to write  python django framework code that is clean and tested using  unit testing ,Test Driven Development.
# new changes comming
The library management system is going to be dockerrize with docker composer, PostgreSQL , Gunicorn and nginx 
## project is live and running on heroku
- live link: https://mighty-sea-09546.herokuapp.com/catalog/
- Login admin creditials:
- https://mighty-sea-09546.herokuapp.com/admin
- username:admin
- password:1111
## How to run The project Local on windows

To get started please ensure that python 3.8 or above is installed in your system


- To run the project locally first of all clone the repository 
  ```
  git clone https://github.com/LomNtetha/Library-Management-System.git
  ```
- go to project directory
  ```
  cd Library-Management-System
  ```

- Create virtual environment
  ```
  python -m venv env
  ```
- Activate the virtual environment
  ```
  env/Scripts/activate
  ```

- Install requirements file
  ```
  pip install -r requirements.txt
  ```

- migrate Database
  ```
  py manage.py migrate
  ```

- Create super user
  ```
  py manage.py createsuperuser
  ```

- run the project
  ```
  py manage.py runserver
  ```

## How to push the project on cloud Heroku PAAS

install heroku cli and git on you system and create  account on heroku

- on project directory
  ```
  git add .
  ```

  
- commit changes
 ```
 git commit -m "My comments"
 ```
     
- create project name
  ```
  heroku create
  ```

- Ensure that projet repostory is listed
  ```
  git remote -v
  ```

- push the project to heroku
  ```
  git push heroku master
  ```

- Create migrations and super user
  ```
  heroku run python manage.py migrate
  ```

  ```
  heroku run python manage.py createsuperuser
  ```

- open the project
  ```
  heroku open
  ```

## packages used 
- python 3.10.2 local and python 3.10.6 on heroku
- Django 4.1
- Sqlite local and postgresql heroku
- whitenoise  6.2.0 for static files
- bootstrap 5
- gunicorn 20.1.0 for http and https server request
 
