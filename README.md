## REST API, based on django, to implement a Release Dashboard

This project provides a REST API to create/read/update/delete:
* Projects
* Environments
* Events
* Statuses

Installation:
-------------
* Clone repository   
`git clone https://github.com/sebbrochet/django_dashboard.git`
* cd into project directory   
`cd django_dashboard`
* Install requirements with pip   
`pip install -r requirements.txt`
* Prepare database and create django superadmin access   
`python manage.py syncdb`
* Sync tables   
`python manage.py migrate`
* Run server   
`python manage.py runserver`

REST API schema is then available at [http://localhost:8000/api/v1](http://localhost:8000/api/v1)

For a more traditional documentation you can read [restapi.md](https://github.com/sebbrochet/django_dashboard/blob/master/restapi.md)
