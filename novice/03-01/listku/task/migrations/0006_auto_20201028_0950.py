# Generated by Django 2.2 on 2020-10-28 09:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0005_auto_20201028_0805'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='Nama',
            new_name='name',
        ),
    ]