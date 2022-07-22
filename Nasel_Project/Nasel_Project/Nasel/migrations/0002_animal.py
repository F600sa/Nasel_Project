# Generated by Django 4.0.6 on 2022-07-22 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Nasel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('age', models.IntegerField()),
                ('photo', models.URLField()),
                ('father', models.CharField(max_length=200)),
                ('mother', models.CharField(max_length=200)),
                ('family', models.CharField(max_length=200)),
            ],
        ),
    ]
