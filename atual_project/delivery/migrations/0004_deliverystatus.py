# Generated by Django 4.2.6 on 2023-10-12 20:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0003_alter_deliveryroute_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeliveryStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Delivered', 'Delivered')], default='Pending', max_length=10)),
                ('route', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='delivery.deliveryroute')),
            ],
        ),
    ]
