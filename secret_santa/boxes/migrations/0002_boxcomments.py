# Generated by Django 4.0.4 on 2022-09-14 18:52

import uuid

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("boxes", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="BoxComments",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True
                    ),
                ),
                ("comment_text", models.TextField(blank=True, null=True)),
                (
                    "box",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="boxcomments", to="boxes.boxes"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="boxcomments",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Comment",
                "verbose_name_plural": "Comments",
            },
        ),
    ]
