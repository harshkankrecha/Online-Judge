# Generated by Django 4.2.3 on 2023-07-17 17:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contests', '0012_alter_score_last_accepted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='score',
            name='last_accepted',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 27, 17, 24, 25, 832150, tzinfo=datetime.timezone.utc)),
        ),
    ]