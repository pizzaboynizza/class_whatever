from django.shortcuts import render
from django.http import HttpResponse
from .models import GroceryItem

def myView(request):
    all_grocery_items = GroceryItem.objects.all()
    return render(request, 'groceries.html',
    {'all_items': all_grocery_items})

# Create your views here.
