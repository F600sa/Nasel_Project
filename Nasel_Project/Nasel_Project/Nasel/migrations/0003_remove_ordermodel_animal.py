# Generated by Django 4.0.6 on 2022-07-27 21:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Nasel', '0002_remove_ordermodel_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordermodel',
            name='Animal',
        ),
    ]
