# Generated by Django 2.2 on 2020-10-28 07:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='Nama_Makanan',
            new_name='Nama',
        ),
    ]