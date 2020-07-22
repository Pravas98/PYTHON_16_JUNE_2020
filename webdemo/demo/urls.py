from django.urls import path
from . import views

urlpatterns = [
    path("index/", views.index),
    path("countries/", views.list_countries),
    path("country/", views.get_country_info),
]
