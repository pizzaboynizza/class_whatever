from django.db import models
import datetime
from django.utils import timezone


class GroceryItem(models.Model):
    items = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    complted = models.DateTimeField('completed date')
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.items
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(day=1)

    def wascomplted(self):
        return self.complted >= timezone.now() - datetime.timedelta(day=1)

    def donelist(self):
        return self.done
    

