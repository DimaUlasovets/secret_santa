# Generated by Django 4.0.4 on 2022-06-03 17:11

import api.models
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="boxes",
            name="status_box",
            field=models.CharField(
                choices=[("open", "open"), ("moving", "moving"), ("close", "close")],
                default=api.models.StatusChoices["OPEN"],
                max_length=10,
            ),
        ),
        migrations.AlterField(
            model_name="giftrequest",
            name="box",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, related_name="giftrequests", to="api.boxes"
            ),
        ),
        migrations.AlterField(
            model_name="giftrequest",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, related_name="giftrequests", to="api.users"
            ),
        ),
    ]