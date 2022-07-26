#/bin/bash

# Init
python -m venv venv --copies
if [[ -f ./venv/bin/activate ]]
then
  source ./venv/bin/activate
else
  source ./venv/Scripts/activate
fi
pip install -r requirements.txt

# Actions
./docker_images.py
./git_sync.py

# Cleanup
