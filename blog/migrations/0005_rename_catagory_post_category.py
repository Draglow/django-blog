# Generated by Django 5.0.3 on 2024-03-13 11:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0004_rename_visibility_post_catagory"),
    ]

    operations = [
        migrations.RenameField(
            model_name="post", old_name="catagory", new_name="category",
        ),
    ]
