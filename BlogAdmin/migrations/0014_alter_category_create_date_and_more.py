# Generated by Django 4.0 on 2021-12-27 06:03

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('BlogAdmin', '0013_alter_category_create_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 27, 6, 3, 23, 209544, tzinfo=utc), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='category',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 27, 6, 3, 23, 209557, tzinfo=utc), verbose_name='date updated'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 27, 6, 3, 23, 208627, tzinfo=utc), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
