from django.urls import path
from . import views


urlpatterns = [
    path('sightings', views.list_sightings),
    path('sightings/stat', views.stat_sighting),
    path('sightings/add', views.add_sighting),
    path('sightings/<str:unique_squirrel_id>', views.edit_sighting),
]
