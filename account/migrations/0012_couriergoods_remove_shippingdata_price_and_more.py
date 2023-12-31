# Generated by Django 4.2.5 on 2023-09-17 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0011_delete_couriergoods_delete_goods_shippingdata_price_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourierGoods',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Weight', models.FloatField(null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='shippingdata',
            name='price',
        ),
        migrations.RemoveField(
            model_name='shippingdata',
            name='weight',
        ),
        migrations.AlterField(
            model_name='personaldata',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='personaldata',
            name='phn',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='shippingdata',
            name='Goodscategory',
            field=models.CharField(choices=[('Electronics', 'Electronics'), ('Fasion', 'Fasion'), ('Accessories', 'Accessories'), ('Books', 'Books'), ('Home Appliances', 'Home Appliances')], default='Books', max_length=200),
        ),
        migrations.AlterField(
            model_name='shippingdata',
            name='shippingaddr',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='store',
            name='contact',
            field=models.IntegerField(null=True),
        ),
    ]
