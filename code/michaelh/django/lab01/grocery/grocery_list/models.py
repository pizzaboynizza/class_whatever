from django.db import models
from django.utils import timezone

class GroceryItem(models.Model):
    text = models.CharField(max_length = 200)
    created_date = models.DateTimeField(default=timezone.now)
    completed_date = models.DateTimeField(blank=True, null=True)
    was_completed = models.BooleanField(default=False)

    def complete(self):
        self.completed_date = timezone.now()
        self.was_completed = True
        self.save()

    def __str__(self):
        return self.text
    