# Generated by Django 3.1.1 on 2021-04-06 20:49

import datetime

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20210402_1235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participation',
            name='enroll_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 6, 23, 49, 36, 590530), verbose_name='Enroll date'),
        ),
    ]
