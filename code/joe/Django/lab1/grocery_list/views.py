from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.utils import timezone

from .models import GroceryItem

def index(request):
    return render(request, "grocery_list/index.html", {"item_list" : GroceryItem.objects.order_by("is_completed", "-date_completed", "date_created")})

def delete(request): # page with checkboxes to delete from list
    return render(request, "grocery_list/delete.html", {"item_list" : GroceryItem.objects.order_by("-is_completed", "date_completed", "-date_created")})

def complete(request): # page with checkboxes to signify completion
    return render(request, "grocery_list/complete.html", {"item_list" : GroceryItem.objects.order_by("is_completed", "-date_completed", "date_created")})

def actual_add(request): # actually add something to the list
    try:
        temp = GroceryItem(text_description=request.POST["item"], date_created=timezone.now())
    except KeyError:
        return render(request, "grocery_list/index.html", {"error": "An error occurred", "item_list" : GroceryItem.objects.order_by("is_completed", "-date_completed", "date_created")})
    else:
        temp.save()
        return HttpResponseRedirect(reverse("grocery_list:index"))

def actual_delete(request): # actually delete things from the list
    try:
        for checked in request.POST.getlist("delete"):
            temp = get_object_or_404(GroceryItem, pk=checked)
            temp.delete()
    except KeyError:
        return render(request, "grocery_list/delete.html", {"error": "An error occurred", "item_list" : GroceryItem.objects.order_by("-is_completed", "date_completed", "-date_created")})
    else:
        return HttpResponseRedirect(reverse("grocery_list:index"))

# TODO: give user datetime to enter for date_completed
def actual_complete(request): # actually check things as complete
    try:
        for checked in request.POST.getlist("complete"):
            temp = get_object_or_404(GroceryItem, pk=checked)
            temp.is_completed = True
            temp.date_completed = timezone.now()
            temp.save()
    except KeyError:
        return render(request, "grocery_list/complete.html", {"error": "An error occurred", "item_list" : GroceryItem.objects.order_by("is_completed", "-date_completed", "date_created")})
    else:
        return HttpResponseRedirect(reverse("grocery_list:index"))