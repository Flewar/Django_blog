# Generated by Django 2.2.7 on 2019-12-06 16:01

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2019, 12, 6, 16, 1, 33, 329464, tzinfo=utc)),
        ),
    ]