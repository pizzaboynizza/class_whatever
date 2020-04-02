from django.shortcuts import render
from django.http import HttpResponse

def grocery_list_app(request):
    return HttpResponse("Active")

