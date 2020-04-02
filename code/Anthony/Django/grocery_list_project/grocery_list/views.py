from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    template = GroceryItem.object.get_template('index.html')
    context = {
        'grocery' :"list here"

    }
    return HttpResponse(template.render(context, request))