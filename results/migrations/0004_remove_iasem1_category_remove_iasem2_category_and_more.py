# Generated by Django 4.0.4 on 2022-05-15 10:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0003_rename_afc_iasem1_foc'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='iasem1',
            name='category',
        ),
        migrations.RemoveField(
            model_name='iasem2',
            name='category',
        ),
        migrations.RemoveField(
            model_name='iasem3',
            name='category',
        ),
        migrations.RemoveField(
            model_name='iasem4',
            name='category',
        ),
    ]
