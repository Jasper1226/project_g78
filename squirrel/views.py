from django.shortcuts import render
from django.http import HttpResponse

class MapView(TemplateView):
    """ View for performing the  sightings' map"""

    template_name = 'squirrel/map.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['sightings'] = models.Sighting.objects.all()
        return ctx
