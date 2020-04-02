from django.shortcuts import render
from .models import GroceryItem
from django.views import generic

def index(request):
    grocery_list = GroceryItem.objects.order_by('-created_date')
    return render(request, 'grocery_list/index.html', {'grocery_list': grocery_list})