from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from django.db import IntegrityError

from .models import UrlShortener, UserLinkData
import random
import string


def index(request):
    return render(request, "url_shortener/index.html")


def newCode(): # generate a new, unique, random code
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
    redirect_link = get_object_or_404(UrlShortener, short_code=goto)
    try:
        user = UserLinkData.objects.filter(user_ip=request.META["REMOTE_ADDR"], user_agent=request.META["HTTP_USER_AGENT"], link_clicked=redirect_link)
        if user.count() > 0:
            user = user[0]
            user.times_clicked += 1
        else:
            user = UserLinkData(user_ip=request.META["REMOTE_ADDR"], user_agent=request.META["HTTP_USER_AGENT"], link_clicked=redirect_link)
        # print(user)
        user.save()
    except KeyError:
        print("User analysis error") # something went wrong with getting things from request.META
    return HttpResponseRedirect(redirect_link.long_link)


def stats(request, goto):
    link = get_object_or_404(UrlShortener, short_code=goto)
    all_users = UserLinkData.objects.filter(link_clicked__exact=link).order_by("user_ip", "-times_clicked")
    return render(request, "url_shortener/stats.html", context={"all_users": all_users, "link": link})


