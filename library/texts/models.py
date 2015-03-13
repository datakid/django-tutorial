""" models.py 
    contains the models for:
    books, sourcetexts and translated texts
    authors, translators
"""

from django.db import models

LANGUAGE_CHOICES = (
  (u'it', u'Italian'),
  (u'ja', u'Japanese'),
  (u'es', u'Spanish'),
  (u'zh-cn', u'Simplified Chinese'),
  (u'zh-tw', u'Traditional Chinese'),
  (u'en', u'English'),
)


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

    def name_length(self):
        return len(self.first)+ len(self.last)

class Translator(models.Model):
    """ The translators """
    first = models.CharField(u'First Name', max_length=30)
    other = models.CharField(u'Other Names', max_length=30, blank=True)
    last = models.CharField(u'Last Name', max_length=30)
    dob = models.DateField(u'Date of Birth', blank=True, null=True)
    original_name = models.CharField(u'Source Name', max_length=40, blank=True)
    language = models.CharField(u'language', max_length=3, choices=LANGUAGE_CHOICES)

    class Meta: 
        ordering = ['last', 'first']
    
    def __unicode__(self):
        return '%s %s' % (self.first, self.last)
    
    def surname_first(self):
        return '%s, %s' % (self.last, self.first) 


class Book(models.Model):
    """ the abstract book model """
    title = models.CharField(u'title', max_length=100)
    publisher = models.CharField(u'publisher', max_length=40)
    date = models.DateField(blank=True, null=True)
    place = models.CharField(u'place', max_length=20)
    pages = models.CharField(u'pages', max_length=5, blank=True)

    class Meta: 
        """ Some meta data """ 
        ordering = ["title"] 
        abstract = True
    
    def __unicode__(self):
        return self.title
        # return '%s, %s, %s' % (self.title, self.publisher, self.place)


class SourceText(Book):
    """ the source text (presumed but not necessarily english) """
    language = models.CharField(u'language', max_length=20, choices=LANGUAGE_CHOICES, default=u'en')
    authors = models.ManyToManyField(Author, verbose_name=u'List of Authors')
    cover_colour = models.CharField('Colour', max_length=10, blank=True)
    cover_colour1 = models.CharField('Colour', max_length=10, blank=True)

class TargetText(Book):
    """ the translated text """
    language = models.CharField(u'language', max_length=20, choices=LANGUAGE_CHOICES)
    source_text = models.ForeignKey(SourceText, related_name=u'source',
                        verbose_name=u'Source Text')
    translators = models.ManyToManyField(Translator, verbose_name=u'List of Translators')

    def __unicode__(self):
        return '%s, %s' % (self.title, self.source.title)
        # return '%s, %s, %s' % (self.title, self.publisher, self.place)
        
