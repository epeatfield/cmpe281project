#CmPE 281
This is a private repo. for CmpE 281

##1) Set up virtual machine
 vagrant up  
 vagrant ssh  
##2) In VM, set up Python3 virtual environment and install these packages
 How to set up Python3 virtual environment in vagrant: https://drive.google.com/file/d/0B9ZdsGRs88lDUUR4dTM3V2dtMDQ/view
 After you already work on your virtual environment, please install these pacakges. 
 Please remember you have to be on your virutal environment of vagrant for any of the following installment.
 
 pip install django==1.11  
 pip install djangorestframework==3.6.2  
 pip install django-model-utils==3.1.1
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
###However, since Thy is working on the models, and she committed the migrations file, 
###so you might not need to run makemigrations command AT THE FIRST TIME SET UP THE PROJECT, simply run migrate to avoid conflicts. If conflicts happen, make your migration files local file, don't commit yours.

###If you are going to change the models, then run makemigrations

  python manage.py makemigrations (DO NOT RUN THIS COMMAND IF YOU INITIALLY SET UP OR DO NOT MAKE ANY CHANGE ON THE MODELS)  
  python manage.py migrate  

##5) In VM, run server
  python manage.py runserver 0.0.0.0:8080   

##6) Django admin - localhost:8082/admin

##7) Creating a Date Time Range Filter
  pip install django-admin-rangefilter==0.3.2

  Make sure 'rangefilter' is added to INSTALLED_APPS in settings.py

##8) Install django-filter
  pip install django-filter==1.1.0  
  This package will help us to add filter on search GET request, for example search sensor data by min value and max value:   
  http://localhost:8082/sensor_data/?min_value=10&max_value=10.6  
  
  Document: https://django-filter.readthedocs.io/en/master/guide/rest_framework.html 
  FUN FACTS (but annoying): the name of pakcage is "django-filter", but you will import "django-filters" 
  And in settings.py, you have to put "django-filters" on top fo the INSTALLED_APPS list. If you put it somewhere else, this package will not be loaded.   
  Still don't know why, but it seems to be conflicted with other packages if you do not put it in the right order. Anyway, the problem is fixed.   
  This stupid thing wasted a lot of my time to figure out :D   
  
  See SensorDataFilter in sensor_data_view.py for more information.  
  
##9) EXPLANATION on how to split models and views to multiple files
  As I said from the begining, Django put all the model classes in one single file named models.py, all the viewapi, viewset, etc classes in one single file named views.py    
  And of course all the serializer classes in one single file named serializers.py   
  
  Each of us will handle one set of models and apis, therefore, if we use the same file, conflict will happen a lot. 
  Therefore, I re-organize the structure so that we can work independently. 
  At the moment, all the model classes are inside models folder, all the view classes are inside views folder, and all the serializers classes are inside serializer folder.   
  This change will not affect how you import a class. For example: from ..models import SensorData => this works for both cases (no matter what one single file or mulitple files for model)   
  Document: https://simpleisbetterthancomplex.com/tutorial/2016/08/02/how-to-split-views-into-multiple-files.html
  
  What will happen when you add an new model class or view model class or serializer class. Goto \_\_init__.py of the corresponding folder and import your newly created class.  
  For example: I create new serialier class named SensorDataSerializer, this is what I add to serializers/\_\_init.py: from water_watch_api.serializers.sensor_data_serializer import SensorDataSerializer
  
##10) EXPLANATION on BATCH INSERT:
  By default, Django POST request will insert one object to database at a time. That says if you need to create 100 objects, you need to call 100 POST requests for each record.  
  That is not performance-wise if you have a lot of data to be created. That is the case for sensor_data, hence, I implemented the BATCH_INSERT POST request for sensor data.  
  If I would like to create 100 objects, I will submit one list of objects in one single POST request.
  I have to do this because my component requires it.
  
  For other tables such as Staion, Sensor Type, Sensor -> the data records are limited in number, so we might not need the BATCH INSERT.
  
##11) Who is responsible for what apis? 
  I put the details here: https://docs.google.com/document/d/1zM4_vTjfsNixK8qcU0VyWiBuvwzj3qCV5-pNMFH0qRc/edit  
  I also put comments inside the \*\_view.py files, please read to get the ideas. And also please refer to our analysis document.  
  If you have any question please let me know.
    
  The sample codes are made fully for SensorType and partly for SensorData.  
  Please read more to understand the differences between retrieve one single record or list all the data based on some filters.   
  Read more about Generics API view - the one we use in our project: http://www.django-rest-framework.org/api-guide/generic-views/
  Remember to add urlPattern to your new apis.
  
##12) One year of real data for 5 stations, each station has 4-6 sensors is committed.
Here is the instruction to import these data to your database: https://docs.google.com/document/d/1ofkzuGExWcZ0Dj3cBtqTie1lMo38Tdpz50o_XceNyf0/edit#heading=h.une83t3i2cfi

##13) We still need fake data to test update/delete/insert api. For example, you can insert 1 row of fake data, test the update api, and then delete it.
Please do not delete/update the real data :D 

##14) API with token based authentication 
Authentication token is a token string generated by the system with enough data to identify a particular user. Please run __python manage.py migrate__ to create new auth tokens table.
Each time an admin user or a non-admin user is created, an authentication token will be automatically generated in this table.  
However, your existing admin user will not have authentication token after this migration. Solution: go to Django admin, open Auth Token -> Tokens table.
Click add token, select your existing admin user and click save, a token will be generated for that admin user.  
Although this is the most simple kind of authenticaton token, it is recommended when we go live to production, we MUST use https instead of http. That will be in our TODO list.  
http://www.django-rest-framework.org/api-guide/authentication/#tokenauthentication  
http://cheng.logdown.com/posts/2015/10/27/how-to-use-django-rest-frameworks-token-based-authentication   
POST localhost:8082/api-token-auth/ can be used to get an auth token of a specific user, put { "username" : "your-user-name", "password" : "your-user-password"} in your request body.  

##15) Permission
Our system only allows Admin to update/delete/create data. Searching or listing data is open to all kinds of user. That says our permission can be described as IsAuthenticated (you have to login/signup) and IsAdminOrReadonly.
Django default supports IsAuthenticated but not IsAdminOrReadOnly. Therefore, I create a custom permission to define the IsAdminOrReadOnly.
In your new view class, plese add this line to register for these permissions.  
  from django_filters import rest_framework as filters  
  from rest_framework import permissions as rest_framework_permissions  
  
  class YourView
     permission_classes = (rest_framework_permissions.IsAuthenticated, custom_permissions.IsAdminOrReadOnly)  
##16) Basic Login/Signup/Logout 
This is the home page: http://localhost:8082/. If you already log in, log out option will be showed. If you not login, then login/signup option will be displayed.
Sign up in this page will create a __non-admin user__. If you wish to create another amdin user, use Django admin dashboard or python manage.py createsuperuser command.  
http://localhost:8082/accounts/login/  
http://localhost:8082/accounts/signup/  
Of course when you sign up for a new user, its authentication token will be generated automatically. 
These login and signup pages are ugly without style. TODO: style them in next component. 

##17) How to test your api with authentication token and permission  
Take this api as an example: http://localhost:8082/sensor_type/  
a) Login as an admin user or non-admin user first and use Django API template on browser to test   
Admin user will be able to search/get/update/add/delete data  
Non-Admin user can only do search/get data  
b) If you do not login, you will get 401 error  
c) Test using postman  
In POST/GET/PUT requests header, add Authorization : Token 7a08c34ad15437d56e5bbd379f94377be8e44bc0 (this is an token example, you have to use your own token)  
d) You can use curl, httpie tool to test your apis. There is a lot of tools out there.  

##18) New packages installation  
pip install django-widget-tweaks==1.4.2  
pip install django-filter==1.1.0 --upgrade  

##19)
Widget Tweaks is an helpful package which help us to break down the form elements like i showed you.  
https://simpleisbetterthancomplex.com/2015/12/04/package-of-the-week-django-widget-tweaks.html    
https://simpleisbetterthancomplex.com/tutorial/2016/11/28/how-to-filter-querysets-dynamically.html  
For example in our login view: 

{% extends 'base.html' %}  
{% load widget_tweaks %}  
{% block title %}Login{% endblock %}  

{% block content %}  
<h2>Login</h2>  
<form method="post">  
  {% csrf_token %}  
  {{ form.username.label_tag }}  
  {% render_field form.username class="form-control" %}  
    {{ form.password.label_tag }}  
  {% render_field form.password class="form-control" %}  
  <button type="submit">Login</button>  
</form>  
{% endblock %}  

##20)
Install GeoDjango
sudo apt-get install binutils libproj-dev gdal-bin  
sudo apt install postgis  
psql <db name>  or use: sudo -u postgres psql
> CREATE EXTENSION postgis;   

##21) Station short name
I create a new field called station short name to save a short name of station name (which is long) so that the UI is not broken. Please run python manage.py migrate after you get the latest code.  
Then go to admin page, add short station name for every station you have, name it as short as 2 words. If you get any problem when viewing admin station page, station map page, and dashboar page please let me know immediately.  




  

