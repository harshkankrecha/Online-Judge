# Generated by Django 4.2.3 on 2023-07-18 06:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contests', '0025_alter_score_last_accepted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='score',
            name='last_accepted',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 28, 6, 15, 4, 647208, tzinfo=datetime.timezone.utc)),
        ),
    ]
