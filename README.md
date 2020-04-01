# Django Elective, Mandatory Assignment 01
BA, Web Development / Copenhagen School of Design & Technology

## Library system

__Requirements__
* __asgiref__ version 3.2.7
* __django__ version 3.2.7
* __django-crispy-forms__ version 3.2.7
* __pyts__ version 3.2.7
* __sqlparse__ version 3.2.7
* Note: this project uses Bootstrap4


### How to use project

__SETUP__
* Create virtual environment and cd into it
* Activate virtual environment
* To install this project's requirements, run ```pip install -r requirements.txt```
* Go nuts!

### Documentation

__APPS__
* Config: The inital project app created on ```django-admin startproject config```
* Library: Handles the inventory of the library; books and authors.
* Membership: Handles user registration, loans, profiles, etc.

__Generic HTML template__
* Located in ```config/templates/base.html```

__Static files__
* CSS located in ```config/static/css/style.css```