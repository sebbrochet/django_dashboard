from tastypie.resources import ModelResource
from restapi.models import Project, Environment, Status, Event
from tastypie.authorization import Authorization

class ProjectResource(ModelResource):
    class Meta:
        queryset = Project.objects.all()
        resource_name = 'projects'
        authorization= Authorization()

class EnvironmentResource(ModelResource):
    class Meta:
        queryset = Environment.objects.all()
        resource_name = 'environments'
        authorization= Authorization()

class EventResource(ModelResource):
    class Meta:
        queryset = Event.objects.all()
        resource_name = 'events'
        authorization= Authorization()

class StatusResource(ModelResource):
    class Meta:
        queryset = Status.objects.all()
        resource_name = 'statuses'
        authorization= Authorization()
