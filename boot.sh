#!/usr/bin/env bash

export FLASK_CONFIG="production"
. pyenv/bin/activate
gunicorn "app:create_app()" -b 127.0.0.1:8000 --reload --max-requests 1