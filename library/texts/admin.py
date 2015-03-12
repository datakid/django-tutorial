from django.contrib import admin

from texts.models import Author, Translator, SourceText, TargetText
# Register your models here.

admin.site.register(Author)
admin.site.register(Translator)
admin.site.register(SourceText)
admin.site.register(TargetText)
