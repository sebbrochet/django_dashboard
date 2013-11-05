from tastypie.resources import ModelResource
from restapi.models import Project, Environment, Status, Event

class ProjectResource(ModelResource):
    class Meta:
        queryset = Project.objects.all()
        resource_name = 'projects'

class EnvironmentResource(ModelResource):
    class Meta:
        queryset = Environment.objects.all()
        resource_name = 'environments'

class EventResource(ModelResource):
    class Meta:
        queryset = Event.objects.all()
        resource_name = 'events'

class StatusResource(ModelResource):
    class Meta:
        queryset = Status.objects.all()
        resource_name = 'statuses'
