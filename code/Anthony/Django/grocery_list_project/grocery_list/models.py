import datetime
from django.db import models
from django.utils import timezone






class GroceryItem(models.Model):
    grocery_text = models.CharField(max_length = 20)
    # /*date list was created*/
    created_date = models.DateTimeField(" date created")  
    completed_date = models.DateField("Date completed")

    def __str__(self):
        return self.grocery_text
    
    def was_published_recently(self):
        return self.completed_date >= timezone.now() -datetime.timedelta(days=1)
  
    
class AddedItem(models.Model):
    groceryItem= models.ForeignKey(GroceryItem, on_delete=models.CASCADE)
    added_item_text = models.CharField(max_length = 20)
  

    def __str__(self):
        return self.added_item_text