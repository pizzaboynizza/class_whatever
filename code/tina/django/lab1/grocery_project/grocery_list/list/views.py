from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone

from .models import GroceryItem

def index(request):
    context = {'':GroceryItem.objects.filter(done=False).order_by('pub_date')}
    return render(request, "list/input.html", context)

def Itemlist(request,GroceryItem_id):
    item = get_object_or_404(GroceryItem,pk=items_id)
    return render(request, 'list/input.html', {'item': item})


def add(request):
    GroceryItem.objects.create(items=request.POST['itemsg'],pub_date=timezone.now())
    return HttpResponseRedirect(reverse('list:index'))
