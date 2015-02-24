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

* This was a system that I actually implemented for Translation and 
Interpreting Studies, School of Languages, Literatures, Cultures & 
Linguistics, Monash University, in 2008, and the data has been absorbed 
into the Austlit Database under the name "Windows on Australia".



Preamble
========

We have an ubuntu 14.04 LTS stable machine, which has postgresql installed,
because it is our preferred database software.

We also have a virtual environment set up, to compartmentalize our python
libraries from the main operating system libraries. 

In the virtualenv we have installed Django and the python connector for 
postgresql:

pip install django psycopg2

We are now ready to start.





Create a project
================

We will presume you are in the directory you would like to be in and in the
virtualenv which has django and psycopg2 installed.


