# Generated by Django 3.0.5 on 2020-04-06 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping_list_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='items_list',
            name='amount',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]