# Generated by Django 5.0 on 2023-12-19 13:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Publicacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('imagen', models.ImageField(upload_to='blog/images')),
                ('date', models.DateField(verbose_name=datetime.date.today)),
            ],
        ),
    ]