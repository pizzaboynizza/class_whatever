from django.urls import path

from . import views

app_name = "grocery_list"
urlpatterns = [
    path("", views.index, name="index"),
    path("complete/", views.complete, name="complete"),
    path("delete/", views.delete, name="delete"),
    path("do_add/", views.actual_add, name="actual_add"),
    path("do_complete/", views.actual_complete, name="actual_complete"),
    path("do_delete/", views.actual_delete, name="actual_delete"),
]