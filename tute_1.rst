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

Preliminary Steps
=================

----------------
Create a project
----------------

We will presume you are in the directory you would like to be in and in the
virtualenv which has django and psycopg2 installed.

Our research will have a title, and this will be the project. A project can
be made of smaller apps, but are all collected together. Think in terms of
having multiple sheets in the same spreadsheet file - each sheet fulfils a
different purpose, even if their data may overlap.

We are going to call our project library.

::

    (venv)$ django-admin.py startproject library

This will create a library directory, with a bunch of files in it.

::

    ├── library
    │   ├── library
    │   │   ├── __init__.py
    │   │   ├── settings.py
    │   │   ├── urls.py
    │   │   └── wsgi.py
    │   └── manage.py


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
that were set up earlier::

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
some of the default tables that Django needs to do it's job. To do this we will need to change into our new project directory.

::

    (venv)$ cd library
    (venv)library$ python manage.py migrate

We will use this command every time we make a change to the data models.



--------------------
Create our first app
--------------------

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
for improvement and as our users ask for more capabilities.

.. note::
    
    There is lots over overlooked dark magic going on under the hood.
    I am deliberately not showing this because it can be arcane and isn't
    stritly necessary to get from where you are to getting a DB working.
    In someways this information can be valuable, and if you decide that
    a Django based database is for you, it will be worth investigating 
    further (the Django site has a great intro tutorial). But suffice to 
    say that it is out of scope for today.



We have already used the name library for the project, so let's call the app 
"texts". With a few exceptions, you can call the project and the app almost
anything you would like. The convetion is to use a hyphen for multi word needs.

::

    (venv)library$ python manage.py startapp texts

If we take a look at what was created, we can see some new files:

::

    ├── library
    │   ├── library
    │   │   ├── __init__.py
    │   │   ├── __init__.pyc
    │   │   ├── settings.py
    │   │   ├── settings.pyc
    │   │   ├── urls.py
    │   │   └── wsgi.py
    │   ├── manage.py
    │   └── texts
    │       ├── admin.py
    │       ├── __init__.py
    │       ├── migrations
    │       │   └── __init__.py
    │       ├── models.py
    │       ├── tests.py
    │       └── views.py

We now have a directory called texts, and within that a number of files.
Straight up I'll say teh __init__.py, the migrations directory and the 
tests.py we will not be using today and are somewhat esoteric anyway. Any
Djangoistas that are reading this will kick my arse for saying don't worry 
about tests, but seriously, don't worry about tests for another year.

So there are three other files. We are literally halfway to a functional 
database.

* models.py is where we describe our data and what we can do to our data.
* views.py is where we describe exactly how we want to manipulate our data, 
    depending on URL.
* admin.py is the simplest way we can build an interface to our data
    (ie, "the website")

==================
The Down and Dirty
==================

Open models.py in an editor and we add this:

::

    """ models.py 
        contains the models for:
        books, sourcetexts and translated texts
        authors, translators
    """
    from django.db import models


The first five lines are a comment that tell us what is in this file and what
we expect it to do. This is merely good practice rather than necessary.

The sixth line tells us (and the software) we will be using the Django model 
system.

Let's build an initial model for our data. We put this in the models.py file, 
directly below the import command:

::

    class Author(models.Model):
        """ The underlying model for writers """
        first = models.CharField(u'First Name', max_length=30)
        other = models.CharField(u'Other Names', max_length=30, blank=True)
        last = models.CharField(u'Last Name', max_length=30)
        dob = models.DateField(u'Date of Birth', blank=True, null=True)

Breaking this down - we are creating a class called a Author. This will be a db
table, and you should think of it in relation to a page on a spreadsheet.

Each author will have a first name, an other name, a last name and a date of 
birth. Each of the name fields is made up of characters ("CharField"), has 
a special name (u'First Name' for ease of use later, and a maximum length.

You will note that the other field has "blank=True". This means that sometimes
we will enter a writer that will not have an other name and that is ok. This
is one of the ways that Django and the database make sure that your data is 
of the correct type.

Finally you will see that dob is a DateField, a special type of field that 
is optimised for dates and date calculations (eg: today-yesterday=1 day) and
"null=True", which is similar to "blank=True". Yse both are necessary and no
I wont explain the difference unless you insist. Again, it's arcane and 
generally unnecessary.

So we have a writer. Let's make a translator:

::

    LANGUAGE_CHOICES = (
      (u'it', u'Italian'),
      (u'ja', u'Japanese'),
      (u'es', u'Spanish'),
      (u'zh-cn', u'Simplified Chinese'),
      (u'zh-tw', u'Traditional Chinese'),
      (u'en', u'English'),
    }

    class Translator(models.Model):
        """ The translators """
        first = models.CharField(u'First Name', max_length=30)
        other = models.CharField(u'Other Names', max_length=30, blank=True)
        last = models.CharField(u'Last Name', max_length=30)
        dob = models.DateField(u'Date of Birth', blank=True, null=True)
        original_name = models.CharField(u'Source Name', max_length=40, blank=True)
        language = models.CharField(u'language', max_length=3, choices=LANGUAGE_CHOICES)
   

Ok, now we have some more interesting work. The Translator is very similar to 
an Author. The main changes are a new name ("original_name"), which is included 
so that we can have the romanised version of their name in the same name space 
as the Author's, but so we can also have their untranslated name.

Finally we have the language field. Note that it is a character field, with a 
max length, but also the "choices" field. And you will note that we have 
defined a small collection of languages. In the available choices, Italian 
will be stored in the database as "it", but we will see it written as 
"Italian". 

When we build the website front end, by describing language like this means we will
see a drop down list of languages rather than an open text field. Adding a new
language is as easy as adding a new line to the LANGUAGE_CHOICES dictionary, eg::

    ('kl', 'Klingon'),

This is easy right?

Let's create a book model:

::

    class Book(models.Model):
      """ the abstract book model """
      title = models.CharField(u'title'), max_length=100)
      publisher = models.CharField(u'publisher', max_length=40)
      date = models.DateField(blank=True, null=True)
      place = models.CharField(u'place', max_length=20)
      pages = models.CharField(u'pages', blank=True)

TODO - Lachlan, look into the DateField and see how to enter the year only, as 
that is a sufficient level of precision for year of publish.

Nothing you haven't seen here, you could have done this yourself at this point.
Some brief explanations. date is date pubished - some books are published 
multiple times, often with new or changed content, so this is important when
we are looking at the source text of a translation. 

Place is because sometimes a large publishing company will print different 
in different countries (or the same book in different territories, etc).

You will see that pages is a character field, even though it will be number. 
We only use the IntegerField when we want to do mathematics on the data. We
will not want to do any pages maths - we are collecting this as "meta-data" 
in order to distinguish between different published copies of the same book.

Now, there are two types of books - source and target - and we don't want to 
code more than we have to. So let's reuse that Book class to make our next
models:

::

    class SourceText(Book):
      """ the source text (presumed but not necessarily english) """
      language = models.CharField(u'language', max_length=20, choices=LANGUAGES, default=u'en')
      authors = models.ManyToManyField(Author, verbose_name=u'List of Authors')

Note two important points here. When we define SourceText, we make it a copy of
the Book model instead of the models.Model. This means that it will have all 
the things that a Book has, as well as the new fields we created. 

The other thing to note is that we have now linked the Book and the Author. 
And you can see that we have acknowledged that some texts have more than one
Author by making it a ManyToManyField. This means "any one Book can have one 
or Many Authors; and any Author may be linked to one or many Books". There 
is no particular reason to attach authors to books, rather than books to 
authors except it seems more intuitively correct. There is no absolute 
correct though, and the changes needed would be minor to flip it.


Because we have created the SourceText as an extension of the Book model, 
we need to add a little to the Book model:

::

    class Book(models.Model):
        """ the abstract book model """
        title = models.CharField(u'title'), max_length=100)
        publisher = models.CharField(u'publisher', max_length=40)
        date = models.DateField(blank=True, null=True)
        place = models.CharField(u'place', max_length=20)
        pages = models.CharField(u'pages', blank=True)

        class Meta: 
            """ Some meta data """ 
            ordering = ["title"] 
            abstract = True

Here you can see I'm telling Django that when you list Books, I want them 
listed alphabetically. Abstract means that there will never actually be a 
Book object, only SourceText objects. Let's see why:

::

    class TargetText(Book):
        """ the translated text """
        language = models.CharField(u'language', max_length=20, choices=LANGUAGES)
        source_text = models.ForeignKey(SourceText, related_name=u'source',
                        verbose_name=u'Source Text')
        translators = models.ManyToManyField(Translator, verbose_name=u'List of Translators')

Here we get to see the last of our real models. There's nothing surprising 
here, but importantly you can see that we are making sure that a Translated
Text is connected to a Source Text. We make this a ForeignKey because any
particular Translated Text will be based off only one SourceText. We think
of this like "any one Translated Text will only have a single Source Text; 
any SourceText may have one or many Translated Texts" - a one to many 
relationship compared to the many to many of the books/author's relationship
described above.

In the TargetText, you will see that the sourec_text link also has the option 
"related_name=u'source'". This gives us a lot of power later - when we are
searching for all the translated texts for a particular source text we can 
access those books by calling the target_text.source field.

TODO - Lachlan, check that the last sentence is true and makes sense.



POtential: Use this for search:
https://github.com/etianen/django-watson/blob/master/README.markdown
