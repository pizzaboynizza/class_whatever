from django.db import models

# Create your models here.

class Item(models.Model):
  name = models.Charfield(max_length=32)
  description = models.TextField()

  def __str__(self):
      return self.name