# Generated by Django 5.1.2 on 2024-10-18 07:37

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("classifier", "0008_alter_requesthistory_response"),
    ]

    operations = [
        migrations.RenameField(
            model_name="plantimage",
            old_name="promo",
            new_name="plant",
        ),
    ]
