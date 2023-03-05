from django.contrib import admin

# Register your models here.
from . models import BackendArt


class BackendArtAdmin(admin.ModelAdmin):
    list_display=['title', 'author', 'upload_art', 'description']

admin.site.register(BackendArt, BackendArtAdmin)