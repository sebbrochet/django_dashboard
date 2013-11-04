from django.contrib import admin
from restapi.models import Project, Environment, Status, Event

admin.site.register(Project)
admin.site.register(Environment)
admin.site.register(Status)
admin.site.register(Event)
