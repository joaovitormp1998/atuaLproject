# Generated by Django 4.2.6 on 2023-10-19 20:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0010_alter_product_foto'),
    ]

    operations = [
        migrations.AddField(
            model_name='deliveryroute',
            name='delivery_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
