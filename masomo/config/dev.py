import os

from .base import *

SECRET_KEY = "django-insecure-l5#*$v6%ntl7w19$w&(fq!dx(_9m%6q%%&$yh-nn-h$1ty-y7m"

DEBUG = True

ALLOWED_HOSTS = ["*"]


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}
