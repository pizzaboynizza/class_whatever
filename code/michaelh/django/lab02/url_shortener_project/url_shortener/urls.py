from django.urls import path
from . import views

# app_name = 'url_shortener' # for namespacing
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:url_code_code>', views.redirect, name='redirect'),
    path('<int:url_code_code>/results', views.results, name='results'),
]