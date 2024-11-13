#!/bin/bash

set -e

# Install Python dependencies
pip install -r requirements.txt

python manage.py collectstatic --no-input
# Run database migrations
python manage.py migrate

# Collect static files
