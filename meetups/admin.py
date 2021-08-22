from django.contrib import admin
from .models import Location, Meetup, Participant

# Register your models here.
@admin.register(Meetup)
class MeetupAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'slug', 'date', 'location']
    list_filter = ('location', 'date')
    prepopulated_fields = {'slug':('title',)}


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'adress']

@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    list_display = ['id', 'email']