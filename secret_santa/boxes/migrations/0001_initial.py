# Generated by Django 4.0.4 on 2022-07-07 21:45

import uuid

import boxes.models
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Boxes",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True
                    ),
                ),
                ("name_box", models.CharField(max_length=100)),
                ("create_date", models.DateTimeField(auto_now_add=True)),
                ("end_date", models.DateTimeField(blank=True, null=True)),
                (
                    "status_box",
                    models.CharField(
                        choices=[("open", "open"), ("moving", "moving"), ("close", "close")],
                        default=boxes.models.StatusChoices["OPEN"],
                        max_length=10,
                    ),
                ),
            ],
            options={
                "verbose_name": "Box",
                "verbose_name_plural": "Boxes",
            },
        ),
        migrations.CreateModel(
            name="ReceiverSender",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True
                    ),
                ),
                ("box", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="boxes.boxes")),
                (
                    "receiver",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="receiver",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "sender",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="sender", to=settings.AUTH_USER_MODEL
                    ),
                ),
            ],
            options={
                "verbose_name": "ReceiverSender",
                "verbose_name_plural": "ReceiverSenders",
            },
        ),
        migrations.CreateModel(
            name="GiftRequest",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True
                    ),
                ),
                ("description", models.TextField(blank=True, null=True)),
                (
                    "box",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="giftrequests", to="boxes.boxes"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="giftrequests",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Gift",
                "verbose_name_plural": "Gifts",
            },
        ),
    ]
