from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import GroceryItem

def index(request):
    current_list = GroceryItem.objects.order_by('-date_created')

    return render(request, 'grocery_list/index.html', context={'current_list':current_list})

def add(request):
    add_item=GroceryItem(text=request.POST.get('item'))
    add_item.save()
    return HttpResponseRedirect(reverse('grocery_list:index'))

def update(request):
    for item in request.POST:
        if item.isdigit()==True:
            completed_item= GroceryItem.objects.get(pk=item)
            completed_item.date_completed=timezone.now()
            completed_item.save()
            print(completed_item)
        else:
            pass
        # completed_item= GroceryItem.objects.get(pk=item)
        # print(completed_item)
    

    # completed_items=GroceryItem.objects.filter(request.POST["completed"])
    # completed_items = GroceryItem.objects.filter(date_completed__isnull=False)
    # completed_items.delete()

    # return HttpResponse("Test")

    return HttpResponseRedirect(reverse('grocery_list:index'))

def delete(request):
    for item in GroceryItem.objects.all():
        print(item)
        if item.is_completed():
            item.delete()
        else:
            pass
    return HttpResponseRedirect(reverse('grocery_list:index'))
