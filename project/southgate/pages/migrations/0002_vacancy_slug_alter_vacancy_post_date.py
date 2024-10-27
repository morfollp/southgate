# Generated by Django 5.1.2 on 2024-10-27 21:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacancy',
            name='slug',
            field=models.CharField(default='nil', max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='post_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 10, 28, 2, 41, 0, 257908)),
        ),
    ]