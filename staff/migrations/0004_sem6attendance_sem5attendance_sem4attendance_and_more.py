# Generated by Django 4.0.4 on 2022-05-07 05:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_sem2students_sem3students_sem4students_sem5students_and_more'),
        ('staff', '0003_alter_sem1attendance_subject'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sem6Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Present', 'Present'), ('Absent', 'Absent')], max_length=10)),
                ('semester', models.CharField(default=1, max_length=20)),
                ('subject', models.CharField(choices=[('placeholder', 'placeholder')], default=None, max_length=255)),
                ('date', models.DateField(auto_now_add=True)),
                ('reg_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.sem6students')),
            ],
        ),
        migrations.CreateModel(
            name='Sem5Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Present', 'Present'), ('Absent', 'Absent')], max_length=10)),
                ('semester', models.CharField(default=1, max_length=20)),
                ('subject', models.CharField(choices=[('placeholder', 'placeholder')], default=None, max_length=255)),
                ('date', models.DateField(auto_now_add=True)),
                ('reg_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.sem5students')),
            ],
        ),
        migrations.CreateModel(
            name='Sem4Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Present', 'Present'), ('Absent', 'Absent')], max_length=10)),
                ('semester', models.CharField(default=1, max_length=20)),
                ('subject', models.CharField(choices=[('DATA STRUCTURES WITH PYTHON', 'DATA STRUCTURES WITH PYTHON'), ('OPERATING SYSTEM & ADMINISTRATION', 'OPERATING SYSTEM & ADMINISTRATION'), ('OBJECT ORIENTED PROGRAMMING & DESIGN WITH JAVA', 'OBJECT ORIENTED PROGRAMMING & DESIGN WITH JAVA'), ('Software Engineering principles and practices', 'Software Engineering principles and practices'), ('Indian Constitution', 'Indian Constitution')], default=None, max_length=255)),
                ('date', models.DateField(auto_now_add=True)),
                ('reg_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.sem4students')),
            ],
        ),
        migrations.CreateModel(
            name='Sem3Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Present', 'Present'), ('Absent', 'Absent')], max_length=10)),
                ('semester', models.CharField(default=1, max_length=20)),
                ('subject', models.CharField(choices=[('PYTHON PROGRAMMING', 'PYTHON PROGRAMMING'), ('COMPUTER HARDWARE, MAINTENANCE AND ADMINISTRATION', 'COMPUTER HARDWARE, MAINTENANCE AND ADMINISTRATION'), ('COMPUTER NETWORKS', 'COMPUTER NETWORKS'), ('DATABASE SYSTEM CCONCEPTS & PL/SQL', 'DATABASE SYSTEM CCONCEPTS & PL/SQL'), ('ಸಾಹಿತ್ಯ ಸಿಂಚನ -II/ ಬಳಕೆ ಕನನಡ-II', 'ಸಾಹಿತ್ಯ ಸಿಂಚನ -II/ ಬಳಕೆ ಕನನಡ-II')], default=None, max_length=255)),
                ('date', models.DateField(auto_now_add=True)),
                ('reg_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.sem3students')),
            ],
        ),
        migrations.CreateModel(
            name='Sem2Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Present', 'Present'), ('Absent', 'Absent')], max_length=10)),
                ('semester', models.CharField(default=1, max_length=20)),
                ('subject', models.CharField(choices=[('PROJECT MANAGEMENT SKILLS', 'PROJECT MANAGEMENT SKILLS'), ('STATISTICS AND ANALYSIS', 'STATISTICS AND ANALYSIS'), ('COMMUNICATION SKILLS', 'COMMUNICATION SKILLS'), ('CAEG (COMPUTER AIDED ENGINEERING GRAPHICS)', 'CAEG (COMPUTER AIDED ENGINEERING GRAPHICS)'), ('MULTIMEDIA & ANIMATION', 'MULTIMEDIA & ANIMATION'), ('KANNADA-1', 'KANNADA-1')], default=None, max_length=255)),
                ('date', models.DateField(auto_now_add=True)),
                ('reg_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.sem2students')),
            ],
        ),
    ]