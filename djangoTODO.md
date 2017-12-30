[yw@yanbox ~]$ pwd
/home/yw
# create virtual env for python
[yw@yanbox ~]$ cd fanhuaxiu/

[yw@yanbox fanhuaxiu]$ virtualenv my_project

[yw@yanbox fanhuaxiu]$ cd my_project

# active virtualenv
[yw@yanbox my_project]$ source bin/activate
(my_project) [yw@yanbox my_project]$ pwd
/home/yw/fanhuaxiu/my_project

# install django in current virtualenv
(my_project) [yw@yanbox my_project]$ pip install django

## check in my current virtual env which package are installed
(my_project) [yw@yanbox my_project]$ pip freeze
Django==2.0
pytz==2017.3
(my_project) [yw@yanbox my_project]$ 

https://docs.djangoproject.com/en/2.0/

https://www.youtube.com/watch?v=jBZHSWoTNd8&list=PLHatWD_TKIRuo5Rq13HbrLs7rWK5rGH3r&index=13

### create django project name as fhx
django-admin startproject fhx

### start flx as first django project
(my_project) [yw@yanbox fhx]$ python manage.py runserver
Performing system checks...

December 16, 2017 - 19:18:23
Django version 2.0, using settings 'fhx.settings'
Starting development server at http://127.0.0.1:8000/


### install mysql connector on virtualenv

(my_project) [yw@yanbox my_project]$ pip install mysql-connector-python


