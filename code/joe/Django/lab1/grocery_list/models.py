from django.db import models

class GroceryItem(models.Model):
    text_description = models.CharField(max_length = 200)
    date_created = models.DateTimeField("date created")
    date_completed = models.DateTimeField("date completed", null=True, blank=True)
    is_completed = models.BooleanField()

    def __str__(self):
        return self.text_description

    
