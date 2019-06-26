from django.contrib import admin
from local.models import Gallery


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('court_soccer', 'photo', 'created_at')