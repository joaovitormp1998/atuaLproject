# Generated by Django 4.2.6 on 2023-10-12 21:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0004_deliverystatus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deliverystatus',
            name='route',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='deliverystatus', to='delivery.deliveryroute'),
        ),
    ]