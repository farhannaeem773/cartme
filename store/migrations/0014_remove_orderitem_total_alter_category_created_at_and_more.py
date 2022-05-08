# Generated by Django 4.0.4 on 2022-05-06 15:04

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0013_alter_category_created_at_alter_product_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='total',
        ),
        migrations.AlterField(
            model_name='category',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 6, 15, 4, 44, 991844, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='product',
            name='Created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 6, 15, 4, 44, 992843, tzinfo=utc)),
        ),
    ]
