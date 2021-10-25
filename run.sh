#/bin/bash

# Init
python -m venv venv --copies
source ./venv/Scripts/activate

# Actions
./docker_images.py

# Cleanup
