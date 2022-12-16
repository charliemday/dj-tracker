#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tests.settings")
    os.environ.setdefault("DEBUG", "true")

    from django.core.management import execute_from_command_line

    try:
        execute_from_command_line(sys.argv)
    finally:
        from dj_tracker import tracker

        tracker.stop()
