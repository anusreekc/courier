# Generated by Django 4.2.5 on 2023-09-17 16:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0012_couriergoods_remove_shippingdata_price_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='shippingdata',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='account.personaldata'),
        ),
        migrations.AddField(
            model_name='shippingdata',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
