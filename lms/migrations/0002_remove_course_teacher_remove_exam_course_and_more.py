# Generated by Django 5.0.3 on 2024-03-20 12:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='teacher',
        ),
        migrations.RemoveField(
            model_name='exam',
            name='course',
        ),
        migrations.RemoveField(
            model_name='lecture',
            name='course',
        ),
        migrations.RemoveField(
            model_name='grade',
            name='exam',
        ),
        migrations.RemoveField(
            model_name='grade',
            name='student',
        ),
        migrations.DeleteModel(
            name='Communication',
        ),
        migrations.DeleteModel(
            name='Course',
        ),
        migrations.DeleteModel(
            name='Lecture',
        ),
        migrations.DeleteModel(
            name='Exam',
        ),
        migrations.DeleteModel(
            name='Grade',
        ),
    ]
