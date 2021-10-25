# _git_mgmt
Sync stuff and random integration stuff

## How to use

Execute `./run.sh` to run all sync and integration scripts at once.

### Build and publish images

Execute `./docker_images.py` either through `./run.sh` or manually.

If executed it'll: 
1. Pull all git repositories listed in `./docker_images.yml` (including submodules)
1. Build all Dockerfiles (in the root directory)
1. Push the created docker image to all listed registries (Make sure to `docker login` beforehand)
