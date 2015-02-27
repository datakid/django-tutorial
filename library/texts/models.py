    """ models.py 
        contains the models for:
        books, sourcetexts and translated texts
        authors, translators
    """


from django.db import models

# Create your models here.

class Author(models.Model):
    """ The underlying model for writers """
    first = models.CharField(u'First Name', max_length=30)
    other = models.CharField(u'Other Names', max_length=30, blank=True)
    last = models.CharField(u'Last Name', max_length=30)
    dob = models.DateField(u'Date of Birth', blank=True, null=True)

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


class SourceText(Book):
   """ the source text (presumed but not necessarily english) """
   language = models.CharField(u'language', max_length=20, choices=LANGUAGES, default=u'en')
   authors = models.ManyToManyField(Author, verbose_name=u'List of Authors')



class TargetText(Book):
     """ the translated text """
     language = models.CharField(u'language', max_length=20, choices=LANGUAGES)
     source_text = models.ForeignKey(SourceText, related_name=u'source',
                        verbose_name=u'Source Text')
     translators = models.ManyToManyField(Translator, verbose_name=u'List of Translators')

