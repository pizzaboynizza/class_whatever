from django.db import models
from django.utils import timezone

class GroceryItem(models.Model):
    text= models.CharField(max_length=30)
    date_created= models.DateTimeField(default=timezone.now)
    date_completed = models.DateTimeField(null=True, blank=True)
    
    def is_completed(self):
        return self.date_completed > self.date_created
        
    def __str__(self):
        return self.text
