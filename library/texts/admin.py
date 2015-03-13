from django.contrib import admin
from texts.models import Author, Translator, SourceText, TargetText

class AuthorAdmin(admin.ModelAdmin):
    list_display = ['__unicode__', 'surname_first', 'dob']

admin.site.register(Author, AuthorAdmin)
admin.site.register(Translator)
admin.site.register(SourceText)
admin.site.register(TargetText)
