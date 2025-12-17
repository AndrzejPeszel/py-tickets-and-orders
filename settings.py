import os
from pathlib import Path

# To jest linia, której brakowało (definiuje BASE_DIR)
BASE_DIR = Path(__file__).resolve().parent

# Kluczowe ustawienie dla testów (bez stref czasowych)
USE_TZ = False

INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "db",
]

AUTH_USER_MODEL = "db.User"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# Musisz mieć też zdefiniowany SECRET_KEY, żeby Django ruszyło
SECRET_KEY = "django-insecure-test-key"