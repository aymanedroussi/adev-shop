# Generated by Django 3.0.5 on 2020-05-09 15:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0032_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='date_ordered',
        ),
    ]
