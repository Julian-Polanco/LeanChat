#!/bin/sh

# Exit immediately if a command exits with a non-zero status.
set -e

# Navigate to the source code directory
cd src

# Apply database migrations
echo "Applying database migrations..."
python manage.py migrate --noinput

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput --clear

# Start the production server
# We use Daphne because it's an ASGI server, required for Django Channels (real-time chat).
echo "Starting server..."
daphne -b 0.0.0.0 -p 8000 project.asgi:application

