from django.db import models

# Create your models here.

class Item(models.Model):
  name = models.CharField(max_length=32)
  description = models.TextField()

  def __str__(self):
      return self.name



# a model called GroceryItem which contains a text description, a created date, a completed date, and a boolean representing whether it was completed