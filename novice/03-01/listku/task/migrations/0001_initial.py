# Generated by Django 2.2 on 2020-10-28 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nama_Makanan', models.TextField(default='')),
                ('Warna', models.TextField(default='')),
                ('Jenis_Makanan', models.TextField(default='')),
            ],
        ),
    ]
