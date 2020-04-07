from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('groceryapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroceryListItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
            ],
        ),
        migrations.RemoveField(
            model_name='groceryitem',
            name='quantity',
        ),
        migrations.AddField(
            model_name='grocerylistitem',
            name='grocery_item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='groceryapp.GroceryItem'),
        ),
        migrations.AddField(
            model_name='grocerylistitem',
            name='grocery_list',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='groceryapp.GroceryList'),
        ),
    ]