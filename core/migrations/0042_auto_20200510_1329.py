# Generated by Django 3.0.5 on 2020-05-10 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0041_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='time',
            name='time_now',
            field=models.TimeField(),
        ),
    ]
