# Generated by Django 4.0.4 on 2022-05-05 10:32

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_title', models.CharField(max_length=20)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2022, 5, 5, 10, 32, 58, 230858, tzinfo=utc))),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('Created_at', models.DateTimeField(default=datetime.datetime(2022, 5, 5, 10, 32, 58, 230858, tzinfo=utc))),
                ('price_1', models.DecimalField(decimal_places=2, max_digits=10)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image', models.ImageField(upload_to='shop/images')),
                ('published', models.BooleanField(default=True)),
                ('Featured', models.BooleanField(default=False)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='store.category')),
                ('sizes', models.ManyToManyField(to='store.size')),
            ],
        ),
    ]