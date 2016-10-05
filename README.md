# NBA

sudo apt-get install python-pip

Installation


1.Download
  Now, you need the django-sample-app project files in your workspace:

$ cd /path/to/your/workspace
$ git clone git://github.com/haticeguney/NBA.git projectname && cd projectname

2. Requirements

Right there, you will find the requirements.txt file that has all the great debugging tools, django helpers and some other cool stuff. To install them, simply type:

$ pip install -r requirements.txt


Initialize the database

$ python manage.py makemigrations

$ python manage.py migrate

$ python manage.py createsuperuser

Ready? Go!

$ python manage.py runserver





