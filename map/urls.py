from django.urls import path
from . import views

urlpatterns = [
    path('', views.sighting_map, name='map'),
]

