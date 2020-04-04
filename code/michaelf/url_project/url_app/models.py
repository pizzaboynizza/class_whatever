from django.db import models

class Url(models.Model):
    code=models.CharField(max_length=7)
    long_url=models.TextField()

    def __str__(self):
        return self.long_url
