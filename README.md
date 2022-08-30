# _git_mgmt
Sync stuff and random integration stuff.

Mainly a workaround to the paywalled "git pull" feature of GitLab Free version and the "docker autobuild" of DockerHub

## How to use

Execute `./run.sh` to run all sync and integration scripts at once.

### Build and publish images

Execute `./docker_images.py` either through `./run.sh` or manually.

If executed it'll: 
1. Pull all git repositories listed in `./docker_images.yml` (including submodules)
1. Build all Dockerfiles (in the root directory)
1. Push the created docker image to all listed registries (Make sure to `docker login` beforehand)

### Sync git repositories

Execute `./git_sync.py` either through `./run.sh` or manually.

If executed it'll:
1. Pull all git repositories listed in `./git_sync.yml` (all branches)
1. Push each git repository to all listed remote targets
