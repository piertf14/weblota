from django.contrib import admin
from local.models import Gallery, Local, CourtSoccer


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('court_soccer', 'photo', 'created_at')


@admin.register(Local)
class LocalAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'name', 'created_at')


@admin.register(CourtSoccer)
class CourtSoccerAdmin(admin.ModelAdmin):
    list_display = ('id', 'local', 'name', 'material_type', 'created_at')