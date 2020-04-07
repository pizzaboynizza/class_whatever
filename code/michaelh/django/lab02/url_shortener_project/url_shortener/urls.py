from django.urls import path
from . import views

# app_name = 'url_shortener' # for namespacing
urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.add, name='add'),
    path('<str:url_code_code>', views.show, name='show'),
    path('<str:url_code_code>/results', views.results, name='results'),
]