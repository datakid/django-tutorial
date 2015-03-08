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

----------------------------------------
Notes on Databases and their terminology
----------------------------------------

Before the Structured Query Language, or SQL, was developed, databases were a 
shambles. There was no standardisation, no common idea. Everyone knew databases
were a great idea, but no one had had that breakthrough moment yet. SQL was the
breakthrough moment, where databases - and computing - went from a good idea
to a game changer.

SQL is a standard way to structure a database.

There are many database products - also known as engines, backends, database 
engines, or database backends, you would have heard of some - MySQL, MariaDB,
SQLite, PostgreSQL, MSSQL, Oracle, even MS Access - the list is long. 

Being such a game changer, it is easy to see why people would want to learn SQL.
The problem with teaching SQL is that while it makes for a great backend, is 
relatively simple and clear to convey, it isn't powerful enough on it's own, 
and doesn't show it's best side easily. 

Putting a front end on an database is the easiest way to show it's true power. 

This is one of the hardest concepts in databases to understand. This tutorial
will be teaching you Django. Django makes it easy to build a front end. You 
can use almost any of the backends listed above with Django. You only need
a database within the installed engine, a user and a password. That's the last
interaction you will have with the software that is called the "database 
backend" - which is the *actual* database software.

Fundamentally, this is a problem of language. It is much easier to just call
the whole product a database, even if the actual database product is MySQL 
and the user interface is written in Django.

You could just as easily use Ruby on Rails to build a front end. Wordpress,
Moodle and Drupal are front ends. All are backed by a database software, and
all only require you know the name of the database, the user and the password.

Some, like MS Access, have a front end built in (shudder). Others, like MySQL
and PostgreSQL have a generic software called phpMyAdmin and phpPgAdmin. 

Between Django, phpPgAdmin and the command line, we have three different 
"windows" into the same database. You will see that the command line is 
the closest to the core, phpPgAdmin is the most like Excel, and Django is 
the most powerful for building applications that you might actually use.

That is why we are teaching Django, and not SQL. You will learn some SQL on 
the way, incidentally, but it is somewhat irrelevant. We just want to get on 
with our research. You just want to get on with your research. Let us help 
you do that.

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

