# Generated by Django 4.1.7 on 2023-07-05 06:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contests', '0009_contest_is_active_alter_score_last_accepted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='score',
            name='last_accepted',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 12, 11, 37, 58, 485145)),
        ),
    ]