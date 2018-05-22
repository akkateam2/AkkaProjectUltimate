#AKKAnnuaire 

#### Prerequisits
-python
You must install python. In our project we use the version pythoon=3.5.0

$ sudo apt install python3.5 

By default python is installed on linux (ubuntu)
verify the version already installed :

$ python --version

if version 2 of python is installed ,it is recommended to let the default version (python2) and use version 3:

$ apt-get install python3-pip
verify python3 works fine : 

$ python3 --version 

-Django 
You must install Django with the version 2.0. This version requirs python3.

$ sudo pip3 install Django

-Djangorestframework

$ python3 -m pip install djangorestframework.

You may need to upgrade the pip package:

$ sudo pip3 install --upgrade pip

-pillow 

$ sudo pip install Pillow

-pytz 

$  easy_install --upgrade pytz

-mysql database

it is need to install mysql as database used

$ sudo apt-get install mysql-server
it is necessary to use "root" as user and password because they are already define in the settings.py file of django project. If else, we can modify in this file the password of the database.
$ sudo apt-get install python-mysqldb
$ sudo service mysql status


#### Getting started

To start by creating first a new folder where we would develop. Get into this folder and import the github project with the below command.

$sudo git clone https://github.com/akkateam/AkkaProjectUltimate.git

when you start a new Django project using the command "django-admin startproject AkkaProject". So if you did not remove the initial configurations you should be all set up. The project called 'AkkaProject' has been already created so not need to use this command.

like no need for the application, not need to use the command "django-admin startapp Akkannuaire" because "Akkannuaire" application exist already in the project.

-creating of database
the connection to the mysql database make using the command :
$sudo mysql -u root -p

After connection to mysql database, it is necessary to create a database of the name  "AkkannuaireBD" because this name is already define in the settings.py of django project.
mysql>CREATE DATABASE AkkannuaireBD

migrate django project to mysql database using some below commands :
$ sudo python3 manage.py migrate
$ sudo python3 manage.py makemigrations

if you wan to start the django project , it is need to create a user using the command line just so we can test the login and logout pages.

$ python3 manage.py createsuperuser
Then enter the login information of the superuser who will be need to connect of the django web administration


you can use this below link to understand login administration with django.
https://simpleisbetterthancomplex.com/tutorial/2016/06/27/how-to-use-djangos-built-in-login-system.html

-login 
Enter in the navigator the url to connect to application. Please use the name and password created while creating superuser previously. 
127.0.0.1:8000/login

-django admin
After be to connect in application, in new url we can use this following link to connect in the graphical administration of django.
127.0.0.1:8000/admin
Here, we can create and delete the user or superuser. Also we can define rights to users.

