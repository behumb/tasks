# Generated by Django 3.1.1 on 2021-01-25 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='todo',
            options={'verbose_name': 'ToDo', 'verbose_name_plural': "ToDo's"},
        ),
        migrations.RemoveField(
            model_name='todo',
            name='category',
        ),
        migrations.AddField(
            model_name='todo',
            name='category',
            field=models.ManyToManyField(to='todos.Category'),
        ),
    ]
