# Generated by Django 3.0.5 on 2020-05-08 15:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0025_auto_20200508_1548'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='image_color_default',
            new_name='color_core_default',
        ),
    ]
