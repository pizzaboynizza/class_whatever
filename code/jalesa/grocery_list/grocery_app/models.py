from django.db import models
from django.utils import timezone
import datetime


# This can be done with a single app called grocery_list and model called GroceryItem which contains a text description, a created date, a completed date, and a boolean representing whether it was completed.

# The user should be presented with an input field and a button (in a form). 
# When the clicks the button, it should save the data to the server and show the newly-added item in the list.
#  The user should be presented with a list of incomplete items and a list of complete items. 
# THe user should be able to mark an item complete/incomplete and be able to delete an item.


class Grocery_item(models.Model):
    grocery_item = models.CharField(max_length=200)
    description = models.TextField()
    pub_date = models.DateTimeField('date published')
    completed_date = models.DateTimeField('date completed', blank=True, null=True)
    is_completed= models.BooleanField(default=False)

    def __str__(self):
        return self.grocery_item # return a string representation of grocery_item
    
# create a form in Django
    # input_field
    # submit button












# 1. Remove all the migration files

# 2. Delete db.sqlite3
# rm db.sqlite3

# 3. Create and run the migrations:
# python manage.py makemigrations
# python manage.py migrate

# 4. Sync the database:
# python manage.py migrate --run-syncdb