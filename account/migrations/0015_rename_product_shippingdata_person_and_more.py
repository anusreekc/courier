# Generated by Django 4.2.5 on 2023-09-26 08:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0014_booking'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shippingdata',
            old_name='product',
            new_name='person',
        ),
        migrations.RemoveField(
            model_name='shippingdata',
            name='shipvalue',
        ),
    ]