# Generated by Django 3.0.5 on 2021-08-09 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lattice', '0002_latticetypes'),
    ]

    operations = [
        migrations.CreateModel(
            name='lattice_2D_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identifier', models.CharField(max_length=6)),
                ('a', models.FloatField()),
                ('b', models.FloatField()),
                ('alpha', models.FloatField()),
                ('beta', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='lattice_3D_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identifier', models.CharField(max_length=6)),
                ('a', models.FloatField()),
                ('b', models.FloatField()),
                ('c', models.FloatField()),
                ('alpha', models.FloatField()),
                ('beta', models.FloatField()),
                ('gamma', models.FloatField()),
                ('bravais_types', models.CharField(max_length=255)),
            ],
        ),
    ]
