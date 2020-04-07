from django.urls import path
from . import views

app_name= 'url_app'

urlpatterns=[
    path('', views.submit, name='submit'),
    path('generate/', views.generate, name='generate'),
    path('<str:code>/', views.redirect, name='redirect'),
]