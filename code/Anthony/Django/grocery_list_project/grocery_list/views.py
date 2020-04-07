from django.shortcuts import render
from django.http import HttpResponse
from .models import GroceryItem

# Create your views here.
def index(request):
    # template = GroceryItem.object.get_template('index.html')
    # context = {
    #     'grocery' :"list here"

    # }
    return render(request, "index.html", {})