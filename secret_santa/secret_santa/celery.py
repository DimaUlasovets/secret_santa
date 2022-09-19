from __future__ import absolute_import, unicode_literals

import os
import pathlib

import dotenv
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "secret_santa.settings")

app = Celery("secret_santa")

app.config_from_object("django.conf:settings", namespace="CELERY")

DOT_ENV_PATH = pathlib.Path() / ".env"
dotenv.load_dotenv(DOT_ENV_PATH)

app.autodiscover_tasks()
