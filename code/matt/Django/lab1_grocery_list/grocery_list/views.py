from django.shortcuts import render
from django.http import HttpResponse, Http404

from .models import GroceryItem

def index(request):
    item_list = GroceryItem.objects.order_by('description')
    context = {
        'item_list': item_list
    }
    return render(request, 'grocery_list/index.html', context)