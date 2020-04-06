from django.urls import path

from . import views

app_name = "url_shortener"

urlpatterns = [
    path("", views.index, name="index"),
    path("add/", views.add, name="add"),
    path("stats/<str:goto>/", views.stats, name="stats"),
    path("<str:goto>/", views.redirect, name="redirect"),
]