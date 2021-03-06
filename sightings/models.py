from django.db.models import Model
from django.db import models


class Sighting(Model):
    unique_squirrel_id = models.TextField(primary_key=True)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    hectare = models.TextField(null=True)
    shift = models.TextField(null=True)
    date = models.DateField(null=True)
    hectare_squirrel_number = models.IntegerField(null=True)
    age = models.TextField(null=True)
    primary_fur_color = models.TextField(null=True)
    highlight_fur_color = models.TextField(null=True)
    combination_of_primary_and_highlight_color = models.TextField(null=True)
    color_notes = models.TextField(null=True)
    location = models.TextField(null=True)
    above_ground_sighter_measurement = models.TextField(null=True)
    specific_location = models.TextField(null=True)
    running = models.BooleanField(null=True)
    chasing = models.BooleanField(null=True)
    climbing = models.BooleanField(null=True)
    eating = models.BooleanField(null=True)
    foraging = models.BooleanField(null=True)
    other_activities = models.TextField(null=True)
    kuks = models.BooleanField(null=True)
    quaas = models.BooleanField(null=True)
    moans = models.BooleanField(null=True)
    tail_flags = models.BooleanField(null=True)
    tail_twitches = models.BooleanField(null=True)
    approaches = models.BooleanField(null=True)
    indifferent = models.BooleanField(null=True)
    runs_from = models.BooleanField(null=True)
    other_interactions = models.TextField(null=True)
    lat_lng = models.TextField(null=True)
    zip_code = models.TextField(null=True)
    community_districts = models.TextField(null=True)
    borough_boundaries = models.TextField(null=True)
    city_council_districts = models.TextField(null=True)
    police_precincts = models.TextField(null=True)

# Create your models here.
