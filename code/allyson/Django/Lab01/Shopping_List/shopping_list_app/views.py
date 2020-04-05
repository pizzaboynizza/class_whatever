from django.http import HttpResponse
from django.shortcuts import render, reverse
from .models import Items_List
from django.template import loader
from django.utils import timezone


def shopping_list_app(request):
    latest_add = Items_List.objects.order_by("-add_date".filter(completed=False))
    pur_item = Item_List.objects.filter(completed=True).order_by("-com_date")
    context - {
        "shop_list": latest_add,
        "purchased": pur_item,
    }
    return render(request, "shopping_list_app/index.html", context)


def add_item(request):
    print = "=" * 100
    print(request.POST)
    add_item_new = request.POST["item_id"]
    new_item = Items_List(text=add_item_new, completed=False, add_date=timezone.now())
    new_item.save()
    return HttpResponse(reverse(""))


def remove_item(request):
    rem_item_id = request.POST["delete_item_id"]
    rem_item = Items_List.objects.get(id=rem_item_id)
    rem_item.delete()
    return HttpResponse(reverse(""))


def undo(request):
    undo = request.POST("undo_item_id")
    undo_item = Items_List.objects.get(id=undo)
    undo_item.completed = False
    undo_item.com_date = None
    undo_item.save()
    return HttpResponse(reverse(""))


def full_list(request):
    item = request.POST["item_id"]
    list = Items_List.objects.get(id=item)
    list.completed = True
    list.com_date = timezone.now()
    list.save()
    return HttpResponse(reverse(""))
