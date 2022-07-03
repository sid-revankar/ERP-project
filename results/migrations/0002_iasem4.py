# Generated by Django 4.0.4 on 2022-05-14 12:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0006_alter_sem1students_options'),
        ('results', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='IaSem4',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ia', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3')], default=1, max_length=1)),
                ('name', models.CharField(default=None, max_length=100)),
                ('ds', models.IntegerField(default=None)),
                ('osa', models.IntegerField(default=None)),
                ('java', models.IntegerField(default=None)),
                ('se', models.IntegerField(default=None)),
                ('ic', models.IntegerField(default=None)),
                ('category', models.CharField(default='Practical', max_length=9)),
                ('total', models.IntegerField(default=None)),
                ('rollno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.sem4students')),
            ],
            options={
                'verbose_name_plural': 'IA Sem-4',
            },
        ),
    ]
