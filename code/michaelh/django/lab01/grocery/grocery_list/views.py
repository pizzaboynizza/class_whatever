from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone

from .models import GroceryItem

def index(request):
    grocery_list = GroceryItem.objects.order_by('-created_date')
    return render(request, 'grocery_list/index.html', {'grocery_list': grocery_list})

def create(request):
    grocery_item_text = request.POST['text']
    GroceryItem.objects.create(item_text = grocery_item_text, created_date = timezone.now())
    return HttpResponseRedirect(reverse('index'))

def detail(request, grocery_item_id):
    grocery_item = get_object_or_404(GroceryItem, pk = grocery_item_id)
    return render(request, "grocery_list/detail.html", {"grocery_item": grocery_item})

def incomplete(request, grocery_item_id):
    grocery_item = get_object_or_404(GroceryItem, pk = grocery_item_id)
    grocery_item.incomplete()
    grocery_item.save()
    return HttpResponseRedirect(reverse('index'))

def complete(request, grocery_item_id):
    grocery_item = get_object_or_404(GroceryItem, pk = grocery_item_id)
    grocery_item.complete()
    grocery_item.save()
    return HttpResponseRedirect(reverse('index'))

def delete(request, grocery_item_id):
    grocery_item = get_object_or_404(GroceryItem, pk = grocery_item_id)
    grocery_item.delete()
    return HttpResponseRedirect(reverse('index'))