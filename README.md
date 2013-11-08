## django_dashboard: REST API to manage a Release Dashboard

This project provides a REST API to create/read/update/delete:
* Projects
* Environments
* Events
* Statuses

Installation:
-------------
* Clone repository
```git clone https://github.com/sebbrochet/django_dashboard.git```
* Install requirements with pip
```cd django_dashboard && pip install -r requirements.txt```
* Run server
```cd django_dashboard && python manage.py runserver```

REST API schema is then available at http://localhost:8000/api/v1?format=json

For a more traditional documentation you can read restapi.md
