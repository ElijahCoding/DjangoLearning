# Generated by Django 2.2.7 on 2019-11-19 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='vin',
            field=models.CharField(db_index=True, max_length=64, unique=True, verbose_name='Vin'),
        ),
    ]
