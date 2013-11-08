from django.db import models
import datetime

class Project(models.Model):
    creation_date = models.DateTimeField(default=datetime.datetime.now)
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __unicode__(self):
        return self.name

class Environment(models.Model):
    creation_date = models.DateTimeField(default=datetime.datetime.now)
    name = models.CharField(max_length=200)
    description = models.TextField()
    project = models.ForeignKey(Project, related_name = 'environments')
    
    def __unicode__(self):
        return self.name

class Status(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __unicode__(self):
        return self.name

class Event(models.Model):
    date = models.DateTimeField(default=datetime.datetime.now)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    environment = models.ForeignKey(Environment, related_name = 'events') 
    status = models.ForeignKey(Status, blank=True, null=True, related_name = 'events')

    def __unicode__(self):
        return self.subject

