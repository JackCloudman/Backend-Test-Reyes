# Generated by Django 3.0.8 on 2021-06-17 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("menu", "0003_auto_20210615_1637"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="comments",
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
