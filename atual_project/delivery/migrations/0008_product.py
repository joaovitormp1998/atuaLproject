# Generated by Django 4.2.6 on 2023-10-18 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0007_deliveryroute_destination_latitude_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
                ('quantidade', models.PositiveIntegerField(default=0)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]