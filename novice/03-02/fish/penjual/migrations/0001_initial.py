# Generated by Django 2.2 on 2020-11-04 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Penjual',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_penjual', models.TextField(default='')),
                ('nm_penjual', models.TextField(default='default')),
                ('alamat', models.TextField(default='default')),
                ('stok_ikan', models.TextField(default='default')),
            ],
        ),
    ]
