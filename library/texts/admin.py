from django.contrib import admin
from texts.models import Author, Translator, SourceText, TargetText

class AuthorAdmin(admin.ModelAdmin):
    list_display = ['__unicode__', 'surname_first', 'dob', 'name_length']

class TranslatorAdmin(admin.ModelAdmin):
    list_display = ['__unicode__', 'original_name', 'language']
    list_filter = ['language']

class SourceTextAdmin(admin.ModelAdmin):
    list_display = ['title', 'publisher', 'place', 'cover_colour']

class TargetTextAdmin(admin.ModelAdmin):
    list_display = ['title', 'publisher', 'place', 'language']


admin.site.register(Author, AuthorAdmin)
admin.site.register(Translator, TranslatorAdmin)
admin.site.register(SourceText, SourceTextAdmin)
admin.site.register(TargetText, TargetTextAdmin)
