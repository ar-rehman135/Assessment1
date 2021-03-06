# Generated by Django 3.2.12 on 2022-04-07 08:09

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bonds', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bonds',
            name='number_of_bonds',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(10000), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='bonds',
            name='status',
            field=models.CharField(choices=[('Published', 'Published'), ('Sold', 'Sold')], default='Published', max_length=20),
        ),
    ]
