from django.db import models
import datetime

# Create your models here.
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
    project = models.ForeignKey(Project)
    
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
    environment = models.ForeignKey(Environment) 
    status = models.ForeignKey(Status, blank=True, null=True)
