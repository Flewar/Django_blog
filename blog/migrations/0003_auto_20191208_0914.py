# Generated by Django 2.2.7 on 2019-12-08 04:14

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20191206_2101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2019, 12, 8, 4, 14, 20, 835528, tzinfo=utc)),
        ),
    ]