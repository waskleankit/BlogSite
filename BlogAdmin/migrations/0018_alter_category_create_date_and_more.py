# Generated by Django 4.0 on 2021-12-28 13:31

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('BlogAdmin', '0017_alter_category_create_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 28, 13, 31, 21, 775594, tzinfo=utc), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='category',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 28, 13, 31, 21, 775607, tzinfo=utc), verbose_name='date updated'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 28, 13, 31, 21, 775180, tzinfo=utc), verbose_name='date published'),
        ),
    ]
