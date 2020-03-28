from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>Hello</1>, <h3>you're at the polls index!</h3>")


