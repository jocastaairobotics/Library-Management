# Generated by Django 5.0 on 2023-12-06 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='available_quantity',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='book',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]
