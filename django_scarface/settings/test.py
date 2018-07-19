from .base import *
from os.path import join

PYLINT_RCFILE = join(SITE_ROOT, 'pylint.rc')
PEP8_RCFILE = join(SITE_ROOT, 'pep8.rc')

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
}
