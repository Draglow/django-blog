# Generated by Django 5.0.3 on 2024-03-08 15:43

import django.contrib.auth.models
import django.db.models.deletion
import django.utils.timezone
import shortuuid.django_fields
import userauth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
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
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="first name"
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="last name"
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                        verbose_name="active",
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="date joined"
                    ),
                ),
                ("full_name", models.CharField(max_length=100)),
                ("username", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("otp", models.CharField(blank=True, max_length=10, null=True)),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        related_name="user_custom_groups",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        related_name="user_custom_permissions",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "verbose_name": "user",
                "verbose_name_plural": "users",
                "abstract": False,
            },
            managers=[("objects", django.contrib.auth.models.UserManager()),],
        ),
        migrations.CreateModel(
            name="Profile",
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
                    "pid",
                    shortuuid.django_fields.ShortUUIDField(
                        alphabet="abcdefghijklmnopqrstuvwxyz",
                        length=7,
                        max_length=25,
                        prefix="",
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        default="default.jpg",
                        null=True,
                        upload_to=userauth.models.user_directory_path,
                    ),
                ),
                (
                    "cover_image",
                    models.ImageField(
                        blank=True,
                        default="cover.jpg",
                        null=True,
                        upload_to=userauth.models.user_directory_path,
                    ),
                ),
                ("full_name", models.CharField(blank=True, max_length=100, null=True)),
                ("slug", models.SlugField(blank=True, null=True, unique=True)),
                ("date", models.DateTimeField(auto_now_add=True)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE, to="userauth.user"
                    ),
                ),
            ],
        ),
    ]
