# Generated by Django 5.0.3 on 2024-03-09 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="text",
            field=models.TextField(blank=True, null=True),
        ),
    ]
