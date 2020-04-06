from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import GroceryItem

def index(request):
    context = {'':GroceryItem.objects.filter(done=False).order_by('pub_date')}
    return render(request, "list/input.html", context)

def Itemlist(request,items_id):
    item = get_object_or_404(GroceryItem,pk=items_id)
    return render(request, 'list/input.html', {'item': item})


def post(requst):
    Grocery_item = get_object_or_404(GroceryItem,pk=items_id)
    item_text = requst.POST['itemsg_id']
    itemt = (text=item_text, completed=False)
    itemt.save()
    return HttpResponseRedirect(reverse('list:index'))


# def fulllist(request):
#     food = get_object_or_404(GroceryItem)
#     return render(request, 'list/item.html', food)
    