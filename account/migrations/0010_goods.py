# Generated by Django 4.2.5 on 2023-09-17 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_rename_price_shippingdata_shipvalue_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dic', models.CharField(max_length=100)),
            ],
        ),
    ]