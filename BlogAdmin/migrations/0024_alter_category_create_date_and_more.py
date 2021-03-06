# Generated by Django 4.0 on 2022-01-05 06:25

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('BlogAdmin', '0023_posts_image_alter_category_create_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 5, 6, 25, 1, 890752, tzinfo=utc), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='category',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 5, 6, 25, 1, 890765, tzinfo=utc), verbose_name='date updated'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 5, 6, 25, 1, 890397, tzinfo=utc), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='image',
            field=models.ImageField(blank=True, upload_to='img'),
        ),
    ]
