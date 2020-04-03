import datetime
from django.db import models
from django.utils import timezone


class Items_List(models.Models):
    item = models.CharField(max_length=50)
    add_date = models.DateTimeField("date created")
    com_date = models.DateTimeField(null=True, blank=True)
    completed=models.BooleanField(null=True, Blank=True)

    def __str__(self):
        return self.item + ""+"("+str(self.completed)+")"

