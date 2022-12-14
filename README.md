# Library-Management-System
This is the basic library management system that is written with django class based function . The main goal of this system was to write  python django framework code that is clean and tested using  unit testing ,Test Driven Development.
# new changes comming
Project workflow CI/CD pipeline to be add soon , Either github actions or gitlab will be add as workflow for this project 
# System prerequisite
- To Run this project you need to have some basics of Django, Ubuntu and git
- Ensure that ubuntu, python, git, editor (such as VS code), docker and docker composer are installed in your system

## project is live and running on heroku
- live link: https://mighty-sea-09546.herokuapp.com/catalog/
- Login admin creditials:
- https://mighty-sea-09546.herokuapp.com/admin
- username:admin
- password:1111
## How to run The project Local for Development

To get started please ensure that python 3.8 or above is installed in your system


- To run the project locally first of all clone the repository 
  ```
  git clone https://github.com/LomNtetha/Library-Management-System.git
  ```
- go to project directory
  ```
  cd Library-Management-System
  ```
- Remove exisitng volumes
 ```
 docker-compose down -v
 ```
- All0w entrypoint permissions to verify that PostgreSQL is healthy before applying the migrations for Development
  ```
  chmod +x locallibrary/entrypoint.sh
  ```
- Build the images and run the containers
  ```
  docker-compose up -d --build
  ```
- Run the migrations
  ```
  docker-compose exec web python manage.py migrate --noinput
  ```
- Ensure the default Django tables were created
 ```
 docker-compose exec db psql --username=admin --dbname=locallibrary_dev
 ```
 List databases
  ```
  \l
  ```
  connected to database "locallibrary_dev" 
  ```
   \c locallibrary_dev
   ```
 List relations
 ```
 \dt
 ```
 then exit
 ```
 \q
 ```

-  check that the volume was created as well by running
  ```
   docker volume inspect Library-Management-System_postgres_data
   ```
- Create superuser
  ```
  docker-compose exec web python manage.py createsuperuser
  ```
- collect static files
 ```
  docker-compose  exec web python manage.py collectstatic --no-input --clear
  ```
- You should be able to view the page at http://localhost:9000/catalog

- Check for errors in the logs if this doesn't work via 
  ```
  docker-compose logs -f.
  ```
## How to run The project Local for Production with nginx and gunicorn
- Bring the container down
 ```
  docker-compose -f docker-compose.prod.yml down -v
  ```
 
- Allow entrypoint permissions to verify that PostgreSQL is healthy before applying the migrations for production
 ```
 chmod +x locallibrary/entrypoint.prod.sh
 ```
- Build the images and run the containers
 ```
  docker-compose -f docker-compose.prod.yml up -d --build
  ```
- Run migrations
 ```
 docker-compose -f docker-compose.prod.yml exec web python manage.py migrate --noinput
 ```
- Create superuser
 ```
 docker-compose -f docker-compose.prod.yml exec web python manage.py createsuperuser
 ```
- organize static and media files to be serve by nginx
 ```
 docker-compose -f docker-compose.prod.yml exec web python manage.py collectstatic --no-input --clear
 ```
- then visit: http://localhost:5000/catalog/

- if the container fails to start, check for errors in the logs via 
 ```
 docker-compose -f docker-compose.prod.yml logs -f
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

## Technology tools and python packages used to develop this system
- Ubuntu 22.04.1 LTS
- Docker version 20.10.18, build b40c2f6
- docker-compose version 1.29.2, build unknown
- git version 2.34.1
- python 3
- Django 4.1.1
- postgresql
- nginx web server
- gunicorn 20.1.0 for http/https server request and WSGI server
- flake8
- Entrypoint shell
- bootstrap 5

 
