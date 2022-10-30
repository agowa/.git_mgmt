#/bin/bash

# Init
export SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
export GIT_SSH_COMMAND="ssh -o ForwardAgent=no -o UserKnownHostsFile='$SCRIPT_DIR/known_hosts' -o ControlMaster=auto -o ControlPersist=60s -o PreferredAuthentications=publickey"
if [ -z $TMUX ]
then
    tmux new-session './run.sh'
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
tmux split-window -d "./docker_images.py; read -p 'Press any key to continue ...'"
tmux split-window -d "./git_sync.py; read -p 'Press any key to continue ...'"

# Cleanup
