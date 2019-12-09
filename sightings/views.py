from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.db.models import Count
from .models import Sighting
from .forms import SightingForm


def list_sightings(request):
    return render(request, 'sightings/sighting_list.html', {
        'sightings': Sighting.objects.all()
    })


def edit_sighting(request, unique_squirrel_id):
    instance = Sighting.objects.get(unique_squirrel_id=unique_squirrel_id)

    if request.method == 'POST':
        form = SightingForm(request.POST, instance=instance)

        if form.is_valid():
            form.save()
            messages.success(request, 'Your changes has been applied')
            return redirect('/sightings/')
        else:
            messages.error(request, form.errors)

    if not Sighting.objects.filter(unique_squirrel_id=unique_squirrel_id).exists():
        return HttpResponse('"%s" does not exist' % unique_squirrel_id)

    return render(request, 'sightings/sighting_edit.html', {
        'form': SightingForm(instance=instance),
    })


def add_sighting(request):
    instance = Sighting()

    if request.method == 'POST':
        form = SightingForm(request.POST, instance=instance)

        if form.is_valid():
            form.save()
            return redirect('/sightings/%s' % form.instance.unique_squirrel_id)
            messages.success(request, 'Your changes was applied')
        else:
            messages.error(request, form.errors)

    return render(request, 'sightings/sighting_add.html', {
        'form': SightingForm(instance=instance),
    })


def stat_sighting(request):
    return render(request, 'sightings/sighting_stat.html', {
        'indicators': [
            ('Number of records', Sighting.objects.count()),
            ('Number of adult squirrels', Sighting.objects.filter(age='ADULT').count()),
            ('Number of shift in PM', Sighting.objects.filter(shift='PM').count()),
            (
                'Distribution of highlight fur color',
                [
                    [x['highlight_fur_color'], x['count']]
                    for x in Sighting.objects.values('highlight_fur_color').annotate(count=Count('highlight_fur_color'))
                ]
            ),
            (
                'Distribution of hectares',
                [
                    [x['hectare'], x['count']]
                    for x in Sighting.objects.values('hectare').annotate(count=Count('hectare'))
                ]
            ),
        ]
    })


# Create your views here.
