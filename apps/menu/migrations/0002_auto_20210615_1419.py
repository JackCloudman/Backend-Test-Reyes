# Generated by Django 3.0.8 on 2021-06-15 14:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("menu", "0001_initial"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="menuoption",
            unique_together={("id_menu", "id_food")},
        ),
    ]
