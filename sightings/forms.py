from django import forms
from .models import Sighting

SHIFT_CHOICES = (('AM', 'AM'), ('PM', 'PM'))


class SightingForm(forms.ModelForm):
    class Meta:
        model = Sighting
        fields = [
            'unique_squirrel_id', 'latitude', 'longitude', 'date', 'shift', 'age', 'primary_fur_color', 'location',
            'specific_location', 'running', 'chasing', 'climbing', 'eating', 'foraging', 'other_activities',
            'kuks', 'quaas', 'moans', 'tail_flags', 'tail_twitches', 'approaches', 'indifferent', 'runs_form',
        ]

    latitude = forms.FloatField(required=True, label='Latitude')
    longitude = forms.FloatField(required=True, label='Longitude')
    unique_squirrel_id = forms.CharField(required=True, label='Unique Squirrel ID')
    date = forms.DateField(required=True, label='Date')
    shift = forms.ChoiceField(required=True, label='Shift', choices=SHIFT_CHOICES)
    age = forms.CharField(required=False, label='Age')
    primary_fur_color = forms.CharField(required=False, label='Primary Fur Color')
    location = forms.CharField(required=False, label='Location')
    specific_location = forms.CharField(required=False, label='Specific Location')
    running = forms.BooleanField(required=False, label='Running', initial=False)
    chasing = forms.BooleanField(required=False, label='Chasing', initial=False)
    climbing = forms.BooleanField(required=False, label='Climbing', initial=False)
    eating = forms.BooleanField(required=False, label='Eating', initial=False)
    foraging = forms.BooleanField(required=False, label='Foraging', initial=False)
    other_activities = forms.CharField(required=False, label='Other Activities')
    kuks = forms.BooleanField(required=False, label='Kuks', initial=False)
    quaas = forms.BooleanField(required=False, label='Quaas', initial=False)
    moans = forms.BooleanField(required=False, label='Moans', initial=False)
    tail_flags = forms.BooleanField(required=False, label='Tail Flags', initial=False)
    tail_twitches = forms.BooleanField(required=False, label='Tail Twitches', initial=False)
    approaches = forms.BooleanField(required=False, label='Approaches', initial=False)
    indifferent = forms.BooleanField(required=False, label='Indifferent', initial=False)
    runs_form = forms.BooleanField(required=False, label='Runs From', initial=False)

    field_order = [
        'latitude', 'longitude', 'unique_squirrel_id', 'shift', 'date', 'age', 'primary_fur_color', 'location', 'specific_location',
        'running', 'chasing', 'climbing', 'eating', 'foraging', 'other_activities', 'kuks', 'quaas', 'moans',
        'tail_flags', 'tail_twitches', 'approaches', 'indifferent', 'runs_form',
    ]

