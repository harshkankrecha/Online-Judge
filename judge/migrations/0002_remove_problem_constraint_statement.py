# Generated by Django 4.2.3 on 2023-07-13 04:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("judge", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="problem",
            name="constraint_statement",
        ),
    ]
