## Django Elective, Mandatory Assignment 01
#### BA, Web Development / Copenhagen School of Design & Technology

This project is a dummy library with user registration, login/logout, permissions and loans. In this initial version, it is required that a staff member with permissions to access the admin paned manually mark a book as status='A' upon deltion of a loan with that instance as primary key.

#### HOW TO USE

* Requirements:
  * __asgiref__ version 3.2.7
  * __django__ version 3.2.7
  * __django-crispy-forms__ version 3.2.7
  * __pyts__ version 3.2.7
  * __sqlparse__ version 3.2.7
  * Note: this project uses Bootstrap4



* Project setup:
  * _Prerequisites: have python3 and django installed on your local machine._
  * Create virtual environment and cd into it
  * Activate virtual environment
  * To install this project's requirements, run ```pip install -r requirements.txt```
  * Go nuts!

#### DOCUMENTATION

* APPS
  * __Config__: The inital project app created on ```django-admin startproject config```. Contains the project's settings file at ``` settings.py ```
  * __Library__: Handles the inventory of the library; books and authors.
  * __Membership__: Handles user registration, login/logout, loans, profiles, etc.

#### GENERIC HTML TEMPLATE
* Located in ```config/templates/base.html```
  * use ``` {% extends 'base.html' %} ``` to use template and extend

#### STATIC FILES
* CSS located in ```config/static/css/style.css```