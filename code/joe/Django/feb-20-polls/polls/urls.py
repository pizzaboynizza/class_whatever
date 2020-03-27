from django.urls import path

from . import views


urlpatterns = [ # this MUST be called urlpatterns
    path("", views.index, name="index"),

]