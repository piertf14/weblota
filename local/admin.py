from django.contrib import admin
from local.models import Gallery, Local, CourtSoccer, Schedule


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('court_soccer', 'photo', 'created_at')


@admin.register(Local)
class LocalAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'name', 'created_at')


@admin.register(CourtSoccer)
class CourtSoccerAdmin(admin.ModelAdmin):
    list_display = ('id', 'local', 'name', 'material_type', 'created_at')


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    raw_id_fields = ('court_soccer', )
    list_display = ('id', 'court_soccer', 'start_time', 'end_time', 'price', 'duration', 'created_at')