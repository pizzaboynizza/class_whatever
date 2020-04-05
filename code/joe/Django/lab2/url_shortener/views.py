from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from django.db import IntegrityError

from .models import UrlShortener
import random
import string


def index(request):
    return render(request, "url_shortener/index.html")


def newCode():
    code = "".join([random.choice(string.ascii_letters + string.digits) for unused in range(0, 6)])
    while UrlShortener.objects.filter(short_code=code).exists(): # must be a unique code
        code = "".join([random.choice(string.ascii_letters + string.digits) for unused in range(0, 6)])
    return code

def add(request):
    message = {}
    try:
        temp = UrlShortener(long_link= request.POST["link"], short_code=newCode())
        temp.save()
        message["success"] = temp
    except KeyError:
        message["msg"] = "There was an error submiting the link"
    except IntegrityError:
        message["msg"] = f"That link already exists!"
        message["success"] = UrlShortener.objects.get(long_link=request.POST['link'])
    
    return render(request, "url_shortener/index.html", context=message)


def redirect(request, goto):
    return HttpResponseRedirect(get_object_or_404(UrlShortener, short_code=goto).long_link)



