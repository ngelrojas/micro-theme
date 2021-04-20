# Generated by Django 3.2 on 2021-04-18 23:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Company",
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
                ("name", models.CharField(max_length=30, unique=True)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("Layoffs", "Layoffs"),
                            ("Hiring Freeze", "Hiring Freeze"),
                            ("Hiring", "Hiring"),
                        ],
                        default="Hiring",
                        max_length=30,
                    ),
                ),
                (
                    "last_update",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                ("application_link", models.URLField(blank=True)),
                ("notes", models.CharField(blank=True, max_length=100)),
            ],
        ),
    ]
