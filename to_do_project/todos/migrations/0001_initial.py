# Generated by Django 3.1.1 on 2021-01-21 10:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
            ],
        ),
        migrations.CreateModel(
            name='TODO',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=300, verbose_name='Text')),
                ('date', models.DateTimeField(auto_now=True, verbose_name='DateTime')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todos.category')),
            ],
        ),
    ]
