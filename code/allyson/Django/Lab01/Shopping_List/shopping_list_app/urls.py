from django.urls import path
from . import views

app_name = "shopping_list_app"

urlpatterns = [
    path("", views.shopping_list_app, name="shopping_list_app"),
    path("static", filename="shopping_list_app/main.css"),
]
