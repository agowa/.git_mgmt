#!/usr/bin/env python3
from tempfile import TemporaryDirectory

import docker
import yaml
from git import Repo

with open("docker_images.yml", "r", encoding="utf-8") as stream:
  try:
    _yaml = yaml.safe_load(stream)
  except yaml.YAMLError as exc:
    print(exc)

for _elem  in _yaml["images"]:
  for _git,_tags in _elem.items():
    with TemporaryDirectory() as _tmp_dir:
      # Clone git repository
      Repo.clone_from(_git, _tmp_dir, multi_options=["--recurse-submodules","--remote-submodules"])
      print(f"Cloned {_git} into {_tmp_dir}")
      # Build docker container
      _client = docker.from_env()
      _image,_ = _client.images.build(path=_tmp_dir, pull=True, rm=True)
      # Tag newly built image
      _image.tag(_tags)
      # Upload image to registries
      for _tag in _tags:
        print(f"Pushing {_git} to {_tag}")
        _repository, _flag = _tag.split(":")
        print("========================================")
        for line in _client.api.push(repository=_repository, tag=_flag, stream=True, decode=True):
          print(line)
        print("========================================")
