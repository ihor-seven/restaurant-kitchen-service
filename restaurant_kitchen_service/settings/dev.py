import os
from .base import BASE_DIR

DEBUG = os.environ.get("DJANGO_DEBUG", "") != "True"

ALLOWED_HOSTS = ["127.0.0.1"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
