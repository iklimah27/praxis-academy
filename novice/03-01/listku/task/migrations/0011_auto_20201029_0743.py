# Generated by Django 2.2 on 2020-10-29 07:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0010_auto_20201029_0723'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='Jenis_Makanan',
            new_name='jenis_makanan',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='Warna',
            new_name='warna',
        ),
    ]