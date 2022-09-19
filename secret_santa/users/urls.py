from django.conf.urls import include
from django.urls import re_path

urlpatterns = [
    re_path(r"v1/", include("users.api.v1.urls")),
]
