# 0x15-API

This project introduces learners to understanding APIs.

The [JSONPlaceholder REST API](https://jsonplaceholder.typicode.com/) was provided for this project.


##  What is an API?
An API, or Application Programming Interface, is a set of protocols, tools, and routines for building software applications. APIs provide a way for different software applications to communicate with each other, allowing developers to integrate external services into their own applications.

## What is RESTful API?
REST, or Representational State Transfer, is a software architectural style that defines a set of constraints to be used when creating web services. A RESTful API is an API that conforms to these constraints.

### Key Concepts

* API: An interface that allows applications to communicate with each other.

* REST: An architectural style that defines a set of constraints for building web services.

* RESTful API: An API that conforms to the constraints defined by the REST architectural style.

* Resources: Data objects that can be accessed and manipulated through the API.

* HTTP Methods: Verbs used to interact with resources, including GET, POST, PUT, PATCH, and DELETE.

#### RESTful API Design Principles
To design a RESTful API, developers should consider the following principles:

* Client-Server Architecture: Separating the user interface concerns from data storage concerns.

* Statelessness: Each request from client to server must contain all of the information necessary to understand the request, and cannot rely on any context stored on the server.

* Cacheability: Responses to requests must be able to be cached or not cached by clients.

* Layered System: A client cannot tell whether it is connected directly to the end server or to an intermediary along the way.

* Uniform Interface: The same resource should be accessible through a consistent interface, regardless of the type of resource or the location of the resource.

#### RESTful API Best Practices
To create a well-designed RESTful API, developers should follow these best practices:

* Use nouns instead of verbs in endpoints.

* Use HTTP methods correctly, such as GET for reading data and POST for creating data.

* Use HTTP status codes correctly, such as 200 for a successful response and 404 for a resource not found.

* Support versioning to allow future changes without breaking existing clients.

* Provide comprehensive documentation for the API.


## Tasks :page_with_curl:

* **0. Gather data from an API**
  * [0-gather_data_from_an_API.py](./0-gather_data_from_an_API.py): Python script
  that returns information on the to-do list progress of a given employee ID.
  * Usage: `python3 0-gather_data_from_an_API.py <employee ID>`.
  * Output: `Employee <employee name> is done with tasks(<# completed tasks>/<total # tasks>):`

* **1. Export to CSV**
  * [1-export_to_CSV.py](./1-export_to_CSV.py): Python script exports to-do list
  information of a given employee ID to CSV format.
  * Usage: `python3 1-export_to_CSV.py <employee ID>`
  * File name: `<user id>.csv`.
  * Format: `"<user id>","<username>","<task completed status>","<task title>"`.

* **2. Export to JSON**
  * [2-export_to_JSON.py](./2-export_to_JSON.py): Python script that exports
  to-do list information of a given employee ID to JSON format.
  * Usage: `python3 2-export_to_JSON.py <employee ID>`
  * File name: `<user id>.json`
  * Format: `{ "<user id>": [ {"task": "<task title>", "completed": <task completed status>, "username": "<username>"}}, ... ]}`

* **3. Dictionary of list of dictionaries**
  * [3-dictionary_of_list_of_dictionaries.py](./3-dictionary_of_list_of_dictionaries.py):
  Python script that exports to-do list information for all employees to JSON format.
  * Usage: `python3 3-dictionary_of_list_of_dictionaries.py`
  * File name: `todo_all_employees.json`
  * Format: `{ "<user id>": [ {"username": "<username>", "task": "<task title>", "completed": <task completed status>}, {"username": "<username>", "task": "<task title>", "completed": <task completed status>}, ... ], "<user id>": [ {"username": "<username>", "task": "<task title>", "completed": <task completed status>}, {"username": "<username>", "task": "<task title>", "completed": <task completed status>}, ... ]}`
