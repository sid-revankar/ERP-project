# Generated by Django 4.0.4 on 2022-05-07 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0003_alter_sem1attendance_subject'),
        ('students', '0002_feedback_remove_student_db_sl_no_student_db_reg_no_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sem2Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=255)),
                ('lname', models.CharField(max_length=255)),
                ('reg_no', models.CharField(blank=True, max_length=10, null=True)),
                ('gender', models.CharField(max_length=1)),
                ('birth_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Sem3Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=255)),
                ('lname', models.CharField(max_length=255)),
                ('reg_no', models.CharField(blank=True, max_length=10, null=True)),
                ('gender', models.CharField(max_length=1)),
                ('birth_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Sem4Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=255)),
                ('lname', models.CharField(max_length=255)),
                ('reg_no', models.CharField(blank=True, max_length=10, null=True)),
                ('gender', models.CharField(max_length=1)),
                ('birth_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Sem5Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=255)),
                ('lname', models.CharField(max_length=255)),
                ('reg_no', models.CharField(blank=True, max_length=10, null=True)),
                ('gender', models.CharField(max_length=1)),
                ('birth_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Sem6Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=255)),
                ('lname', models.CharField(max_length=255)),
                ('reg_no', models.CharField(blank=True, max_length=10, null=True)),
                ('gender', models.CharField(max_length=1)),
                ('birth_date', models.DateField()),
            ],
        ),
        migrations.RenameModel(
            old_name='student_db',
            new_name='Sem1Students',
        ),
    ]
