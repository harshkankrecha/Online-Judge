# Generated by Django 4.2.3 on 2023-07-15 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("contests", "0005_alter_score_last_accepted"),
    ]

    operations = [
        migrations.AlterField(
            model_name="score",
            name="last_accepted",
            field=models.DateTimeField(),
        ),
    ]