from django.db import models

class URL_Code(models.Model):
    code = models.CharField(max_length = 200)
    url = models.CharField(max_length = 200)
    
    def __str__(self):
        return self.url

class Click(models.Model):
    ip = models.CharField(max_length = 200)
    referer = models.CharField(max_length = 200, blank=True, null=True)
    url_code = models.ForeignKey(URL_Code, on_delete = models.CASCADE)