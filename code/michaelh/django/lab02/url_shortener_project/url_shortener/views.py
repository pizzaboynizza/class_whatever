from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

import string
import random
from .models import URL_Code

def index(request):
    return render(request, 'url_shortener/index.html')

def add(request):
    url_code_url = request.POST['url']
    while True:  
        url_code_code = ''
        for i in range(6):
            url_code_code += random.choice(string.ascii_lowercase+string.digits)
        url_code = URL_Code.objects.filter(code__exact = url_code_code)
        if not url_code:  
            break  
    url_code = URL_Code.objects.create(url = url_code_url, code = url_code_code)
    return HttpResponseRedirect(reverse('results', args = (url_code.code,)))

def show(request, url_code_code):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    print(ip)
    referer = request.META.get('HTTP_REFERER')
    print(referer)

    url_code = URL_Code.objects.get(code__exact = url_code_code)
    return redirect(url_code.url)

def results(request, url_code_code):
    url_code = URL_Code.objects.get(code__exact = url_code_code)
    url_code_code = url_code.code
    return render(request, 'url_shortener/results.html', {'url_code': url_code, 'url_code_code': url_code_code})    
