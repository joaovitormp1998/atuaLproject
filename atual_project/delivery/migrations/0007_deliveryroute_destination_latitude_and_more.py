# Generated by Django 4.2.6 on 2023-10-18 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0006_alter_deliverystatus_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='deliveryroute',
            name='destination_latitude',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True),
        ),
        migrations.AddField(
            model_name='deliveryroute',
            name='destination_longitude',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True),
        ),
    ]
