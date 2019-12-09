from django.shortcuts import render
from sightings.models import Sighting


def sighting_map(request):
    return render(request, 'map/map.html', {
        'sightings': Sighting.objects.all()
    })
# Create your views here.
