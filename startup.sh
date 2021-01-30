#!/bin/bash
gunicorn --bind 0.0.0.0:9000 --workers 1 wsgi:app