#!/usr/bin/env python
import os
import sys

from photos_w_zach.settings import base


def main():
    """Run administrative tasks."""

    # Checks if DEBUG is True/False to load correct settings file (local/prod)
    if base.DEBUG:
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'photos_w_zach.settings.local')
    else:
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'photos_w_zach.settings.prod')

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
