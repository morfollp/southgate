# Generated by Django 5.1.2 on 2024-11-15 18:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacancy',
            name='post_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 11, 16, 0, 3, 49, 756592)),
        ),
    ]
