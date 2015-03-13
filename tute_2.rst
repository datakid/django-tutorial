=================================================
Learning practical databases via a Django web app
=================================================

Tutorial 2
==========

-----------------------------------------------------
In which we bump into and quickly solve easy problems
-----------------------------------------------------

Mandatory Fields and Data Validation
------------------------------------

When you click on the add button next to Authors, you will see the "Add 
author" interface

.. image:: imgs/add_author_1.png

While it's mostly self explanitory, I'll walk you through some of the 
subtlties.

First, notice that First Name and Last Name are in bold? That's because they 
are mandatory fields. If you go back and look at where we defined the Author
model, you will see that we used "blank=True" on two fields. This indicates 
that those fields were **not** mandatory. Anything without "blank=True" is
a mandatory field.

If you try to save an object (an object is an instance of a model) without a 
name, you will see that the admin interface won't let you.

The second and third notable advantages of the admin interface are in the date 
field. You will see that there is, importantly, a very easy "today" button and
calendar to quickly enter dates via mouse. You can obviously type them as well.

The other notable here is what happens when you enter a non date string into 
that field - eg "aaaa". You will see that when you try to save it will be 
rejected as "invalid". 

One of Django's greatest advantages is that when you define a field on a model
Django takes that definition as what constitutes a valid entry. Anything that
isn't valid can't be entered. 

As a database user, this is invaluable. Garbage in, garbage out is a famous
data science saying. Incomplete and poorly formatted data is every data 
scientists worst nightmare. 

Without having to any more work than necessary, we have data validation out of
the box. Django just saved you hours of heartache, which your typing fingers
should appreciate.


Anonymity
---------

After you have saved your first Author object with success you will be taken to
a screen that looks like this

.. image:: imgs/add_author_save_1.png

Looks good. But look what happens when we add another Author.

.. image:: imgs/author_list_1.png

Ok, now we have a problem. We can't tell which object is which author. And 
here, when we add a text, we see the problem compounded - we can't distinguish
the authors from each other to assign one. Bugger.

.. image:: imgs/add_source_text_0.png

Let's fix it.

Crack open *texts/models.py* and find the Author class. We will add a 
**method** to that class.

::

    class Author(models.Model):
        """ The underlying model for writers """
        first = models.CharField(u'First Name', max_length=30)
        other = models.CharField(u'Other Names', max_length=30, blank=True)
        last = models.CharField(u'Last Name', max_length=30)
        dob = models.DateField(u'Date of Birth', blank=True, null=True)

        def __unicode__(self):
            return '%s %s' % (self.first, self.last)

There's a lot in those two lines of code, and we will try to answer as many of
them as possible.

    * When we are programming in this fashion, we define classes of objects and
      we can give those classes, and their resulting objects, *functions*. Those 
      functions are pure programming - from within there you can do whatever 
      you want. Obviously we like to keep them as short and understandable as
      possible, but they will get longer. Functions are "actions" cf the 
      model's fields.
    * Most of the functions you write will not have underscores surrounding 
      them. The reasoning is beyond the scope of this tutorial, suffice to
      say that they are "special internal functions" within Django. 
    * self? WTF is self? Ok. We have a **CLASS** that defines a **MODEL**. 
      That **MODEL** is an abstraction. When we create a new instance of that
      abstraction, we call it an **OBJECT**. Each of those objects will have
      the ability to call any **FUNCTION** associated with it - note the 
      indentation of the function definition being one level in from class 
      definition. The **SELF** is how the function knows which object's 
      variables to use when doing it's actions.
    * In case you missed it, the return line will return the string for the
      object as defined by "firstname lastname" or "<first> <last>". As we
      would expect.
    * This special function is an identity reference on an object and is very
      very useful, as we will see later. Don't worry, I'll point it out when it
      happens.


.. todo:: Is it worth making the analogy to spreadsheets?

          The Model is the spreadsheet page

          The Class is the headings in row 1

          The Object is each line below the heading (the data)

          The Functions are the columns at the end of the Class Fields that reference
          other fields

          The Self is the equivalent of referencing something in the same line in a 
          spreadsheet function - ie the reference to A2 and B2 in col C

          ===== ========= ======== ===================
          index column A  column B column C
          ===== ========= ======== ===================
             1  **First** **Last** **NAME**
             2  Lachlan   Simpson  =STRCAT(A2, B2)
          ===== ========= ======== ===================
 

Ok, now when we refresh the Author list page, we see named objects. That's much
easier to use. 

But, like all good solutions, it now raises two more problems - do the rest of
our models need an identity reference? In our use case, yes. But you wont 
always - that will be something you will need to decide on a per model basis.
The other problem is sort order. In the English speaking world we tend to order
lists of people alphabetically by last name.

I'll leave the first problem as an exercise for the reader.

For the second problem, there are a couple of solutions, which can be done
individually *or* collectively. Let's do them all.

Create a new function
---------------------

Let's make this dead easy and just create a new function that returns "<last>, 
<first>" instead of "<first> <last>".

::

    class Author(models.Model):
        """ The underlying model for writers """
        first = models.CharField(u'First Name', max_length=30)
        other = models.CharField(u'Other Names', max_length=30, blank=True)
        last = models.CharField(u'Last Name', max_length=30)
        dob = models.DateField(u'Date of Birth', blank=True, null=True)

        def __unicode__(self):
            return '%s %s' % (self.first, self.last)

        def surname_first(self):
            return '%s, %s' % (self.last, self.first) 


We can see how this works because we understand programming - we wont see it
in action immediately, but will come back to it.

Add a sort order
----------------

If you recall, when we were defining the Book class as an abstract class, we
also added the Meta variable *ordering*. We can apply this to the Author class
as well.

::
    
    class Author(models.Model):
        """ The underlying model for writers """
        first = models.CharField(u'First Name', max_length=30)
        other = models.CharField(u'Other Names', max_length=30, blank=True)
        last = models.CharField(u'Last Name', max_length=30)
        dob = models.DateField(u'Date of Birth', blank=True, null=True)

        class Meta:
            ordering = ['last', 'first']
            # ordering = ['-last', '-first'] would order reverse alphabetically 
            # ordering = ['last', 'first', 'dob'] would order alpha, then by DOB
    
        def __unicode__(self):
            return '%s %s' % (self.first, self.last)

        def surname_first(self):
            return '%s, %s' % (self.last, self.first) 


Note that the ordering of the functions and the Meta class don't matter, only 
the indentation does. Traditionally we keep them ordered for readability, and 
the order I choose is: Meta, __special_functions__, normal_functions with the 
last two being alphabetically ordered internally.
