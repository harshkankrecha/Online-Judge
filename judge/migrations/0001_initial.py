# Generated by Django 4.1.7 on 2023-06-27 09:59

import ckeditor.fields
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
            name='Problem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('problem_statement', ckeditor.fields.RichTextField()),
                ('code', models.CharField(max_length=255)),
                ('input_statement', ckeditor.fields.RichTextField()),
                ('constraint_statement', ckeditor.fields.RichTextField()),
                ('output_statement', ckeditor.fields.RichTextField()),
                ('editorial', ckeditor.fields.RichTextField(default='Coming Soon')),
                ('users', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Testcases',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('input_file', models.FileField(default=None, upload_to='C:\\Users\\harsh\\Desktop\\oj\\oj/static')),
                ('answer_file', models.FileField(default=None, upload_to='C:\\Users\\harsh\\Desktop\\oj\\oj/static')),
                ('is_sample_testcase', models.BooleanField(default=False)),
                ('problem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='judge.problem')),
            ],
        ),
        migrations.CreateModel(
            name='Solution',
            fields=[
                ('solution_id', models.AutoField(primary_key=True, serialize=False)),
                ('verdict', models.CharField(max_length=50)),
                ('submitted_at', models.DateTimeField()),
                ('submitted_code', models.CharField(max_length=255)),
                ('problem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='judge.problem')),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]