from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Url, Click
from django.urls import reverse
import random, string

def submit(request):
    return render(request, 'url_app/submit.html', context=None)

def generate(request):
    code=''.join(random.choices(string.ascii_lowercase+string.digits, k=7))
    new_url=Url(code=code,long_url=request.POST.get('url'))
    print(new_url)
    new_url.save()
    return render(request,'url_app/generate.html',context={'code': code})

def redirect(request, code):
    fetched_url = get_object_or_404(Url, code=code)
    try:
        click= Click(ip=request.META['REMOTE_ADDR'], click_url=fetched_url, referral=request.META['HTTP_REFERER'])
        click.save()
    except:
        click= Click(ip=request.META['REMOTE_ADDR'], click_url=fetched_url, referral='none')
        click.save()
    print(fetched_url.click_set.count())

    return HttpResponseRedirect(f"{fetched_url}")
    


