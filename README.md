#CmPE 281
This is a private repo. for CmpE 281

##1) Set up virtual machine
 vagrant up  
 vagran ssh  
##2) In VM, set up virtual environment and install these packages
 pip install django==1.11  
 pip install djangorestframework==3.6.2  
##3) In VM, set up PostgreSQL
  sudo apt install postgresql postgresql-contrib  

  sudo -u postgres createuser waterwatchadmin -P  
  (When asked please use this password for user: khongcopw)  
  (DB information can be found in settings.py)  

  sudo -u postgres createdb waterwatch -O waterwatchadmin  
  pip install psycopg2  
  Tutorial video: https://youtu.be/wYqiEUlJrBA
##4) In VM, migrate db
Create admin/superuser for Django admin (one time only):
  python manage.py createsuperuser  

###Every time we make a update/create new models run these commands:  
###However, since Thy is working on the models, and she committed the migrations file, so you might not need to run makemigrations command AT THE FIRST TIME SET UP THE PROJECT, simply run migrate to avoid conflicts. If conflicts happen, make your migration files local file, don't commit yours.

###If you are going to change the models, then run makemigrations

  python manage.py makemigrations  
  python manage.py migrate  

##5) In VM, run server
  python manage.py runserver 0.0.0.0:8080   

##6) Django admin - localhost:8082/admin
