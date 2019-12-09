from django.urls import path
from . import views


urlpatterns = [
    path('', views.list_sightings),
    path('stats/', views.stat_sighting),
    path('add/', views.add_sighting),
    path('<str:unique_squirrel_id>/', views.edit_sighting),
]
