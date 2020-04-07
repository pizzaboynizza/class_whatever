from django.contrib import admin
from .models import UrlShortener, UserLinkData

admin.site.register(UrlShortener)
admin.site.register(UserLinkData)