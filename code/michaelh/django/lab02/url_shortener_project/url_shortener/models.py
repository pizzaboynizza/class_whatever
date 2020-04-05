from django.db import models

class URL_Code(models.Model):
    code = models.CharField(max_length = 200)
    url = models.CharField(max_length = 200)
    
    def __str__(self):
        return self.url