# Generated by Django 5.1.1 on 2024-09-09 10:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("tabom", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="like",
            name="article",
        ),
        migrations.RemoveField(
            model_name="like",
            name="user",
        ),
        migrations.DeleteModel(
            name="Article",
        ),
        migrations.DeleteModel(
            name="Like",
        ),
        migrations.DeleteModel(
            name="User",
        ),
    ]
