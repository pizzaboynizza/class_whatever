# Generated by Django 3.0.5 on 2020-04-06 21:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('url_shortener', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Click',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=200)),
                ('referer', models.CharField(max_length=200)),
                ('url_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='url_shortener.URL_Code')),
            ],
        ),
    ]
