from django.http import HttpResponse
from django.shortcuts import render

import string
import random
from .models import URL_Code

def index(request):
    return render(request, 'url_shortener/index.html')

def add(request):
    url_code_url = request.POST['url']
    url_code_code = ""
    for i in range(6):
        url_code_code += random.choice(string.ascii_lowercase+string.digits)
    url_code = URL_Code.objects.create(url = url_code_url, code = url_code_code)
    return HttpResponseRedirect(reverse('results', args = (url_code.id,)))

def redirect(request, url_code_id):
    url_code = get_object_or_404(URL_Code, pk = url_code_id)
    return HttpResponseRedirect(reverse(url_code.url))

def results(request, url_code_id):
    url_code = get_object_or_404(URL_Code, pk = url_code_id)
    return render(request, 'polls/results.html', {'url_code': url_code})    
