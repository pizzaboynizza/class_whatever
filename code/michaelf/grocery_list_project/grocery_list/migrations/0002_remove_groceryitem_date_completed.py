# Generated by Django 3.0.5 on 2020-04-02 01:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grocery_list', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='groceryitem',
            name='date_completed',
        ),
    ]