# Generated by Django 3.1.1 on 2021-04-12 13:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0012_remove_courseprogress_is_complete'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReadingMaterialProgress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_complete', models.BooleanField()),
                ('course_progress', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.courseprogress')),
                ('reading_material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.readingmaterial')),
            ],
        ),
        migrations.CreateModel(
            name='TestProgress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_complete', models.BooleanField()),
                ('course_progress', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.courseprogress')),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.test')),
            ],
        ),
        migrations.DeleteModel(
            name='TaskProgress',
        ),
        migrations.AddConstraint(
            model_name='testprogress',
            constraint=models.UniqueConstraint(fields=('test', 'course_progress'), name='test_progress'),
        ),
        migrations.AddConstraint(
            model_name='readingmaterialprogress',
            constraint=models.UniqueConstraint(fields=('reading_material', 'course_progress'), name='reading_material_progress'),
        ),
    ]
