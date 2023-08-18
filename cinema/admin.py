from django.contrib import admin
from .models import Branch, Theater, Seat, Movie, Event


class BranchAdmin(admin.ModelAdmin):
    list_display = ['location_name']


admin.site.register(Branch, BranchAdmin)


class TheaterAdmin(admin.ModelAdmin):
    list_display = ['label', 'branch']
    list_filter = ['branch']


admin.site.register(Theater, TheaterAdmin)


class SeatAdmin(admin.ModelAdmin):
    list_display = ['seat_row', 'seat_column', 'theater', 'seat_status']
    list_filter = ['theater']


admin.site.register(Seat, SeatAdmin)


class MovieAdmin(admin.ModelAdmin):
    list_display = ['title', 'duration', 'release_date', 'rating']
    search_fields = ['title']
    list_filter = ['rating']


admin.site.register(Movie, MovieAdmin)


class EventAdmin(admin.ModelAdmin):
    list_display = ['movie', 'theater', 'datetime']
    list_filter = ['theater', 'movie']
    search_fields = ['movie__title']


admin.site.register(Event, EventAdmin)
