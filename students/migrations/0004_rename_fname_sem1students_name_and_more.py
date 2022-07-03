# Generated by Django 4.0.4 on 2022-05-12 12:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_sem2students_sem3students_sem4students_sem5students_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sem1students',
            old_name='fname',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='sem2students',
            old_name='fname',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='sem3students',
            old_name='fname',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='sem4students',
            old_name='fname',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='sem5students',
            old_name='fname',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='sem6students',
            old_name='fname',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='sem1students',
            name='lname',
        ),
        migrations.RemoveField(
            model_name='sem2students',
            name='lname',
        ),
        migrations.RemoveField(
            model_name='sem3students',
            name='lname',
        ),
        migrations.RemoveField(
            model_name='sem4students',
            name='lname',
        ),
        migrations.RemoveField(
            model_name='sem5students',
            name='lname',
        ),
        migrations.RemoveField(
            model_name='sem6students',
            name='lname',
        ),
    ]
