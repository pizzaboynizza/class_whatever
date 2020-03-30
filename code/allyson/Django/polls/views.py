from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello!  You are are my polls index!")
