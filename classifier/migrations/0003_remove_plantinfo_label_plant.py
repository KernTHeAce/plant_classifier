# Generated by Django 5.1.2 on 2024-10-10 14:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("classifier", "0002_plantimage"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="plantinfo",
            name="label",
        ),
        migrations.CreateModel(
            name="Plant",
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
                (
                    "info",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="classifier.plantinfo",
                    ),
                ),
                (
                    "label",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="classifier.label",
                    ),
                ),
            ],
        ),
    ]
