# Generated by Django 3.0.5 on 2020-04-01 22:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GroceryItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=30)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_completed', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
