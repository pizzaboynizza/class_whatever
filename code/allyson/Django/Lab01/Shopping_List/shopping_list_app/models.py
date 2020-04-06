import datetime
from django.db import models
from django.utils import timezone


class Items_List(models.Model):
    item = models.CharField(max_length=50)
    amount = models.PositiveIntegerField()
    add_date = models.DateTimeField("date created")
    com_date = models.DateTimeField(null=True, blank=True)
    completed = models.BooleanField(null=True, blank=True)

    def __str__(self):
        return self.item + "" + "(" + str(self.completed) + ")"
