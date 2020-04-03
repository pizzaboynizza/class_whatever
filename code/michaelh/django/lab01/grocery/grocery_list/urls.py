from django.urls import path
from . import views

# app_name = 'grocery_list'
urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
    path('<int:grocery_item_id>/', views.detail, name='detail'),
    path('<int:grocery_item_id>/delete', views.delete, name='delete'),
    path('<int:grocery_item_id>/incomplete', views.incomplete, name='incomplete'),
    path('<int:grocery_item_id>/complete', views.complete, name='complete'),
]