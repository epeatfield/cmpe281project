#CmPE 281
This is a private repo. for CmpE 281

##1) Set up virtual machine
 vagrant up  
 vagran ssh  
##2) Set up virtual environment
 pip install django==1.11  
 pip install djangorestframework==3.6.2  
##3) Set up PostgreSQL
  sudo apt install postgresql postgresql-contrib  
  sudo -u postgres createuser waterwatchadmin -P  
  sudo -u postgres createdb waterwatch -O waterwatchadmin  
  pip install psycopg2  
##4) Migrate db
  python manage.py createsuperuser  
  python manage.py makemigrations  
  python manage.py migrate  
##5) Run server
  python manage.py runserver 0.0.0.0:8080  
