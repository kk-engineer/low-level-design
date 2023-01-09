# Generated by Django 4.1.5 on 2023-01-07 16:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('parking_lot', '0002_parkingspot_lot_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='entry_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
