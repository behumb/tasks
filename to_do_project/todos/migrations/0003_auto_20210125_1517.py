# Generated by Django 3.1.1 on 2021-01-25 12:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0002_auto_20210125_1326'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='category',
            new_name='categories',
        ),
    ]
