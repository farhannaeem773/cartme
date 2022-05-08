# Generated by Django 4.0.4 on 2022-05-06 14:07

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_orders_alter_category_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 6, 14, 7, 50, 575225, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='product',
            name='Created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 6, 14, 7, 50, 575225, tzinfo=utc)),
        ),
    ]
