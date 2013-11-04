Project
A Project can describes a product, web site or something similar.
A Project is run/tested/experienced on several Environments

. List all projects :
GET http://.../api/projects

. Return a specific project:
GET http://.../api/projects/{id}

. Create a new project: 
POST http://.../api/projects
{
 "name" : {string},
 "description" : {string}
}

. Updates and returns a project:
PUT http://.../api/projects/{id}
{
 "name" : {string},
 "description" : {string}
}

. Delete a project (and associated resources!)
DELETE http://.../api/projects/{id}

Environment
An Environment is where a Project is run/tested/experienced
There can be several different Environment for the same Project.

. List all environments :
GET http://.../api/environments

. List all environments for a specific project:
GET http://.../api/projects/{id}/environments

. Return a specific environment:
GET http://.../api/environments/{id}

. Create a new environment:
POST http://.../api/environments
{
 "name" : {string},
 "description" : {string},
 "project_id" : {integer}
}

. Updates and returns an environment:
PUT http://.../api/environments/{id}
{
 "name" : {string},
 "description" : {string},
 "project_id" : {integer}
}

. Delete an environment (and associated resources!)
DELETE http://.../api/environments/{id}

Event
An Event is something that may happen in the life of an Environment.

. List all events:
GET http://.../api/events

. List all events for a specific environment
GET http://.../api/environments/{id}/events

. List all events for a specific project
GET http://.../api/projects/{id}/events

Filter events by date:
?date=

. Create a new event:
POST http://.../api/events
{
 "subject" : {string}
 "message" : {string}
 "environment_id" : {integer},
 "status_id" : {integer}
}

Status
A Status is an optional parameter to describe an Event.

. List all statuses :
GET http://.../api/statuses

. Return a specific status:
GET http://.../api/statuses/{id}

. Create a new status:
POST http://.../api/statuses
{
 "name" : {string},
 "description" : {string}
}

. Updates and returns a status:
PUT http://.../api/status/{id}
{
 "name" : {string},
 "description" : {string}
}

. Delete a status (and associated resources!)
DELETE http://.../api/statuses/{id}

