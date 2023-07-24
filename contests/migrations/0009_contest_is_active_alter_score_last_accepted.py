# Generated by Django 4.1.7 on 2023-07-05 04:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contests', '0008_alter_score_last_accepted'),
    ]

    operations = [
        migrations.AddField(
            model_name='contest',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='score',
            name='last_accepted',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 12, 9, 51, 27, 381786)),
        ),
    ]