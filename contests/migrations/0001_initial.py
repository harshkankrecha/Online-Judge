# Generated by Django 4.2.3 on 2023-07-07 10:32

import ckeditor.fields
import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Contest",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("description", models.TextField()),
                ("start_time", models.DateTimeField()),
                ("end_time", models.DateTimeField()),
                ("duration_minutes", models.IntegerField()),
                ("is_active", models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="Question",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("problem_statement", ckeditor.fields.RichTextField()),
                ("code", models.CharField(max_length=255)),
                ("input_statement", ckeditor.fields.RichTextField()),
                ("constraint_statement", ckeditor.fields.RichTextField()),
                ("output_statement", ckeditor.fields.RichTextField()),
                ("editorial", ckeditor.fields.RichTextField(default="Coming Soon")),
                ("points", models.IntegerField(default=0)),
                (
                    "contest",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="contests.contest",
                    ),
                ),
                ("users", models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name="Testcases",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("input_file", models.FileField(default=None, upload_to="static/")),
                ("answer_file", models.FileField(default=None, upload_to="static/")),
                ("is_sample_testcase", models.BooleanField(default=False)),
                (
                    "question",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="contests.question",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Submission",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("code", models.TextField()),
                ("language", models.CharField(max_length=50)),
                ("submitted_at", models.DateTimeField(auto_now_add=True)),
                ("verdict", models.CharField(max_length=50)),
                ("submitted_code", models.CharField(max_length=255)),
                (
                    "question",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="contests.question",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Score",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("total_points", models.FloatField(default=0.0)),
                ("penalties", models.IntegerField(default=0)),
                (
                    "last_accepted",
                    models.DateTimeField(
                        default=datetime.datetime(2023, 7, 14, 16, 2, 39, 320850)
                    ),
                ),
                (
                    "contest",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="contests.contest",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
