from django.contrib import admin

from publication.models import Publication, Like

# Register your models here.
admin.site.register(Publication)
admin.site.register(Like)