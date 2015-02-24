=================================================
Learning practical databases via a Django web app
=================================================

Goal
====

We are about to embark on a new research project - creating a collection of
Australian texts that have been translated into foreign languages, 
essentially a small library system*. 

We will need to collect data and have data entry done for us. It's not 
particularly difficult or large data set, but we will need a number of 
research assistants to participate, across different languages, and the 
thought of managing the version control of the spreadsheet is painful. 

In the days before google spreadsheets made collaborative work 
significantly easier, this web application was small and fast to develop, 
and served the same function. 

In this class we hope to show the distinct advantages that a database 
backed small web app has over the relatively simple collaborative
spreadsheet.

Full disclosure: this is a newer version of a system that I actually 
implemented for Translation and Interpreting Studies, School of Languages, 
Literatures, Cultures & Linguistics, Monash University, in 2008, and the 
data has been absorbed into `the Austlit Database under the name "Windows on Australia" <http://www.austlit.edu.au/specialistDatasets/WindowsOnAustralia>`_.


Preamble
========

We have an ubuntu 14.04 LTS stable machine, which has postgresql installed,
because it is our preferred database software.

We also have a virtual environment set up, to compartmentalize our python
libraries from the main operating system libraries. 

In the virtualenv we have installed Django and the python connector for 
postgresql::    

    pip install django psycopg2

We will also presume that there is a database ready within PostgreSQL called
db, accessible by db_user using password db_password. Note that these are 
*terribly* named examples and are used for expediency rather than good 
practice.

We are now ready to start.


What we will learn
==================

0. What are we doing?

We want to learn about databases and how they work - it will help us with
our data gathering, it will help us to mentally *visualise* our data, it 
will give us an easy interface with which to work with our data.

1. Creating a project, and some top level concepts

This will help you get started on your own. We can't abstract this away for
everyone like we can offer a VM with Ubuntu and postgres and a virtenv. It
shows clearly the few commands needed to get started, and does a broad 
brush stroke explanation of what is happening, without getting your hands 
too dirty, or your mind too befuddled.

2. Creating an app, and some mid level concepts

As with above, we do the bare minimum of work and explanation to help you 
proceed, without setting the bar so high you are discouraged - just enough
to get stuff done.

3. Building our web app

This is where you will see the real beauty and power of using a database 
backed web app.


Why a Web App
=============

SQL is very powerful. It's very useful. At the time of the invention of
relational databases and SQL, they were a revelation. The world of 
structured data was changed for ever, and the world itself will never be 
the same. 

They are deep and powerful knowledge management ideas that now probably  
touch 90% of what you do and read online, and effect your lives in ways you
cannot imagine. 

Despite this, or because of it's low level of abstration, SQL is obtuse and
difficult to work with. Computers have advanced enough that we can have 
much prettier interfaces to those databases. What we find happens these 
days is that one type of SQL database or another - MySQL, PostgreSQL, 
SQLITE, MSSQL, the list goes on - sits behind most applications. The front,
user facing, part is another app that sits on top of the database. 

In this case we will be using Django, which is what is known as a Web 
Framework - think like a collection of scaffolding parts with which you can
build any shape building by attaching the parts appropriately and haning 
stuff off them. 

Theory: Database -> Web Framework -> User Interface/CSS
Practice: PostgreSQL -> Django -> Bootstrap

Mostly we will be learning Django and a little Bootstrap. We do not need to 
learn SQL really, we can get Python to do that heavy lifting for us.

Create a project
================

We will presume you are in the directory you would like to be in and in the
virtualenv which has django and psycopg2 installed.

Our research will have a title, and this will be the project. A project can
be made of smaller apps, but are all collected together. Think in terms of
having multiple sheets in the same spreadsheet file - each sheet fulfils a
different purpose, even if their data may overlap.

We are going to call our project library.
::

    $ django-admin.py startproject library

This will create a library directory, with a bunch of files in it.
::

    ├── library
    │   ├── library
    │   │   ├── __init__.py
    │   │   ├── settings.py
    │   │   ├── urls.py
    │   │   └── wsgi.py
    │   └── manage.py
    ├── tute_1.rst


* The top level library is our project. 
* The second level library folder is that which holds the project level 
  details - general settings and URLs. 
    * wsgi.py is part of deployment and we almost certainly wont need to 
      touch it. 
    * __init__.py is a python file that tells python that this is a library
      or an app.
* manage.py is a special file that we also shouldn't need to touch, but 
  helps us manage our Django project from the command line.
  
Once we have made a couple of small changes to these files, we wont need to
come back very often. Most of the work happens in the apps themselves.

We edit library/library/settings.py focusing on these fields, using the details
that were set up earlier:::

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'db',
            'USER': 'db_user',
            'PASSWORD': 'db_password',
            'HOST': '127.0.0.1',
            'PORT': '5432',
        }
    }

Here we have set the database connection. Now we can populate the database with
some of the default tables that Django needs to do it's job.
::
    $ python manage.py migrate





Create our first app
====================

Depending on the size and shape of our data, we may need to do a little bit of 
pen and paper work to determine the best way to break our data down into it's 
constituent parts. In most cases, each app should be relatively small and just 
do one or two things. In this case, we will make our app a little bigger, 
because it will be our only app. 

At the end of this I will give an example of a more complex app and how to go 
about mentally mapping that into applications.

The brief synopsis of what we want is:

 - a collection of books 
    - some of those books will be "source texts" - Australian literature
    - some of those books will be "target texts" - foreign language books with
      at least a link to a "source text"
 - a collection of writers
    - some of those writers will be "source text" Authors. They may have one or
      more "source texts"
    - some of those writers will be Translators. We will presume they have a 
      single language other than English. They may have one or more "target 
      texts". 

In various ways we will want to cross reference and group these texts in a way
that makes investigating the data relatively simple. 

Our app will be based on this simple model, and we will grow it as we see room
for improvement.

::

