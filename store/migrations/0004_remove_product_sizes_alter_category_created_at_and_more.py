# Generated by Django 4.0.4 on 2022-05-06 09:38

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_alter_category_created_at_alter_product_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='sizes',
        ),
        migrations.AlterField(
            model_name='category',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 6, 9, 38, 51, 897747, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='product',
            name='Created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 6, 9, 38, 51, 898747, tzinfo=utc)),
        ),
    ]
