# Generated by Django 4.2.5 on 2023-09-10 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='personaldata',
            name='message',
            field=models.CharField(max_length=500, null=True),
        ),
    ]