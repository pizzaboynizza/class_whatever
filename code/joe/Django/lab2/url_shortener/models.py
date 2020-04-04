from django.db import models

# ☑ Version 1
# ☐ Version 2
# ☐ Version 3

class UrlShortener(models.Model):
    short_code = models.CharField(unique=True, max_length=7)
    long_link = models.CharField(unique=True, max_length=200)

    def __str__(self):
        return f"{self.short_code} : '{self.long_link}'"


