from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import GroceryItem

def Itemlist(request):
    item = GroceryItem.objects.all()
    return render(request, 'lists/input.html', item)

def fulllist(request):
    food = get_object_or_404(GroceryItem)
    return render(request, 'lists/item.html', food)