# Generated by Django 3.1.1 on 2021-01-26 12:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0004_auto_20210125_1723'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Tag',
                'verbose_name_plural': 'Tags',
            },
        ),
        migrations.RemoveField(
            model_name='todo',
            name='categories',
        ),
        migrations.AddField(
            model_name='todo',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='todos.category'),
        ),
        migrations.AddField(
            model_name='todo',
            name='tags',
            field=models.ManyToManyField(to='todos.Tag'),
        ),
    ]
