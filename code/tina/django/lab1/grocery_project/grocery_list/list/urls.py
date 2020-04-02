from django.urls import path, include
from . import views
from django.contrib import admin


app_name = 'list'
urlpatterns = [
    
    path('', views.Itemlist, name='Itemlist')
]
