from django.db import models
from django.utils import timezone
import datetime

# Create your models here.


# class Post(models.Model):
#     author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     title = models.CharField(max_length=200)
#     text = models.TextField()
#     created_date = models.DateTimeField(default=timezone.now)
#     published_date = models.DateTimeField(blank=True, null=True)

#     def publish(self):
#         self.published_date = timezone.now()
#         self.save()

#     def __str__(self):
#         return self.title


class GroceryItem(models.Model):
    description = models.CharField(max_length=500)
    created_date = models.DateTimeField(default=timezone.now)
    is_completed = models.BooleanField(default=False)
    completed_date = models.DateTimeField(blank=True, null=True)

    def completed(self):
        self.completed_date = timezone.now()
        self.save()
    
    def __str__(self):
        return self.description

    