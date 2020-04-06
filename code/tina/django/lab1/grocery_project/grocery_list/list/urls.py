from django.urls import path, include
from . import views
from django.contrib import admin


app_name = 'list'
urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('Itemlist/', views.Itemlist, name='Itemlist'),
]
