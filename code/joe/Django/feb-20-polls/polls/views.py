# from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Hello!</h1><h3>You're at the polls index!</h3>")