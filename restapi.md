###Project
A Project can describe a product, web site or something similar.  
A Project is run/tested/experienced on several Environments.

* List all projects 

`GET http://.../api/projects?format=json`

* Return a specific project:

`GET http://.../api/projects/{id}?format=json`

* Create a new project: 

`POST http://.../api/projects?format=json`

With body:
`{   
 "name" : {string},     
 "description" : {string}      
}`

* Updates and returns a project

`PUT http://.../api/projects/{id}?format=json`

With body:
`{
 "name" : {string},
 "description" : {string}
}`

* Delete a project (and associated resources!)

`DELETE http://.../api/projects/{id}?format=json`

###Environment
An Environment is where a Project is run/tested/experienced.   
There can be several different Environment for the same Project.

* List all environments

`GET http://.../api/environments?format=json`

* List all environments for a specific project

`GET http://.../api/environments?project={id}?format=json`

* Return a specific environment

`GET http://.../api/environments/{id}?format=json`

* Create a new environment

`POST http://.../api/environments`

With body:
`
{
 "name" : {string},
 "description" : {string},
 "project_id" : {integer}
}`

* Updates and returns an environment

`PUT http://.../api/environments/{id}?format=json`

With body:
`
{
 "name" : {string},
 "description" : {string},
 "project_id" : {integer}
}`

* Delete an environment (and associated resources!)

`DELETE http://.../api/environments/{id}?format=json`

###Event
An Event is something that may happen in the life of an Environment.

* List all events

`GET http://.../api/events?format=json`

* List all events for a specific environment

`GET http://.../api/events?environment={id}?format=json`

* List all events for a specific project

`GET http://.../api/events?environment__project={id}?format=json`

* Create a new event

`POST http://.../api/events?format=json`

With body:
`{
 "subject" : {string}
 "message" : {string}
 "environment_id" : {integer},
 "status_id" : {integer}
}`

###Status
A Status is an optional parameter to describe an Event.

* List all statuses

`GET http://.../api/statuses?format=json`

* Return a specific status

`GET http://.../api/statuses/{id}?format=json`

* Create a new status

`POST http://.../api/statuses?format=json`

with body:
`{
 "name" : {string},
 "description" : {string}
}`

* Updates and returns a status

`PUT http://.../api/status/{id}?format=json`

With body:
`{
 "name" : {string},
 "description" : {string}
}`

* Delete a status (and associated resources!)

`DELETE http://.../api/statuses/{id}?format=json`
