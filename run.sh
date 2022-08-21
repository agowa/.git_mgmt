#/bin/bash

# Init
if [ -z $TMUX ]
then
    tmux new-session -d './run.sh' \; attach
    exit $?
fi
python -m venv venv --copies
if [[ -f ./venv/bin/activate ]]
then
  source ./venv/bin/activate
else
  source ./venv/Scripts/activate
fi
pip install -r requirements.txt

# Actions
tmux split-window -d "./docker_images.py"
tmux split-window -d "./git_sync.py"

# Cleanup
