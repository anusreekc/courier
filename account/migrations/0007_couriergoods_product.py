# Generated by Django 4.2.5 on 2023-09-17 04:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_rename_weights_couriergoods_weight'),
    ]

    operations = [
        migrations.AddField(
            model_name='couriergoods',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='account.personaldata'),
        ),
    ]
