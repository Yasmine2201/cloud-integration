from django.contrib import admin

from publication.models import Publication, Comment, Like

# Register your models here.
admin.site.register(Publication)
admin.site.register(Comment)
admin.site.register(Like)