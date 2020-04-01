from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import GroceryItem

def index(request):
    return render(request, "grocery_list/index.html", {"item_list" : GroceryItem.objects.all()})


def add(request): # page with form to add things to list
    pass

def delete(request): # page with checkboxes to delete from list
    pass

def actual_add(request): # actually add something to the list
    pass

def actual_delete(request): # actually delete things from the list
    pass