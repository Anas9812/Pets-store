# Generated by Django 4.2.3 on 2023-09-23 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordersapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='status',
            field=models.CharField(choices=[('new', 'new'), ('pending', 'pending'), ('delivered', 'delivered'), ('cancelled', 'cancelled')], default='new', max_length=100),
        ),
    ]
