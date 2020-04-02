from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import GroceryItem

def index(request):
    current_list = GroceryItem.objects.order_by('-date_created')

    return render(request, 'grocery_list/index.html', context={'current_list':current_list})

def add(request, item_text):
    add_item=GroceryItem(text=item_text)
    add_item.save()
    return HttpResponseRedirect(reverse('grocery_list:index'))