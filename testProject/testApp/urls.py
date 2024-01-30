from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("imageanalysis/", views.imageApi, name="imageanalysis"),
]