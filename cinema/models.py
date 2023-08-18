from django.db import models
from django.conf import settings

# Create your models here.





class Branch(models.Model):
    location_name = models.CharField(max_length=30, primary_key=True)

class Theater(models.Model):
    label = models.CharField(max_length=20)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)

    constraints = [
        models.UniqueConstraint(fields=['label', 'branch'], name='unique_label_branch')
    ]


class Seat(models.Model):
    AVAILABLE = 'available'
    BLOCKED = 'blocked'
    RESERVED = 'reserved'

    STATUS_CHOICES = [
        (AVAILABLE, 'Available'),
        (BLOCKED, 'Blocked'),
        (RESERVED, 'Reserved'),
    ]
    seat_status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default=AVAILABLE,
    )

    seat_row = models.IntegerField()
    seat_column = models.IntegerField()
    theater = models.ForeignKey(Theater, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['seat_row', 'seat_column', 'theater'], name='unique_seat_position')
        ]


class Movie(models.Model):
    duration = models.DurationField()
    release_date = models.DateField()
    title = models.CharField(max_length=200, primary_key=True)
    description = models.TextField()
    # MPA Rating System
    G = 'G'  # General Audiences - All Ages Admitted
    PG = 'PG'  # Parental Guidance Suggested - Some Material May Not Be Suitable for Children
    PG13 = 'PG-13'  # Parents Strongly Cautioned - Some Material May Be Inappropriate for Children Under 13
    R = 'R'  # Restricted - Under 17 Requires Accompanying Parent or Adult Guardian
    NC17 = 'NC-17'  # Adults Only - No One 17 and Under Admitted

    RATING_CHOICES = [
        (G, 'G - General Audiences'),
        (PG, 'PG - Parental Guidance Suggested'),
        (PG13, 'PG-13 - Parents Strongly Cautioned'),
        (R, 'R - Restricted'),
        (NC17, 'NC-17 - Adults Only'),
    ]

    rating = models.CharField(max_length=6, choices=RATING_CHOICES, default=G, help_text="MPA Film Rating")

class Event(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    theater = models.ForeignKey(Theater, on_delete=models.CASCADE)
    datetime = models.DateTimeField()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['movie', 'theater', 'datetime'], name='unique_movie_theater_datetime')
        ]















