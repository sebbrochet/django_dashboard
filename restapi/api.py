from tastypie.resources import ModelResource
from restapi.models import Project, Environment, Status, Event
from tastypie.authorization import Authorization
from tastypie import fields
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS

class ProjectResource(ModelResource):
    class Meta:
        queryset = Project.objects.all()
        resource_name = 'projects'
        authorization= Authorization()

        ordering = ['creation_date', '-creation_date']

class EnvironmentResource(ModelResource):
    project = fields.ForeignKey(ProjectResource, 'project')
    class Meta:
        queryset = Environment.objects.all()
        resource_name = 'environments'
        authorization= Authorization()

        ordering = ['creation_date', '-creation_date']

class StatusResource(ModelResource):
    class Meta:
        queryset = Status.objects.all()
        resource_name = 'statuses'
        authorization= Authorization()

class EventResource(ModelResource):
    environment = fields.ForeignKey(EnvironmentResource, 'environment')
    status = fields.ForeignKey(StatusResource, 'status', null=True, blank=True)

    class Meta:
        queryset = Event.objects.all()
        resource_name = 'events'
        authorization= Authorization()

        filtering = {
            'date': ALL,
            'subject': ALL,
            'status': ALL,
            'environment': ALL_WITH_RELATIONS,
        }

        ordering = ['date', '-date']
