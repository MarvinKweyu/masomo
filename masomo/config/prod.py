import os

from .base import *

# Todo replace this with your own secret key
SECRET_KEY = os.getenv(
    "SECRET_KEY", "django-insecure-l5#*$v6%ntl7w19$w&(fq!dx(_9m%6q%%&$yh-nn-h$1ty-y7m"
)

DEBUG = False
ADMINS = (("Masomo Administrator", "email@masomo.com"),)

# Todo replace this with your domain settings

ALLOWED_HOSTS = ["*"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("DATABASE_NAME", "masomo"),
        "USER": os.getenv("DATABASE_USER", "masomo"),
        "PASSWORD": os.getenv("DATABASE_PASSWORD", "masomo"),
    }
}
