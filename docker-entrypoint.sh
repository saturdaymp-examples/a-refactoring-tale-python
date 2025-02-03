#!/bin/sh

# Exit immediately if a command exits with a non-zero status
set -e

# Install Python requirements
pip install -r /app/requirements.txt

# Execute the command passed to the script
exec "$@"