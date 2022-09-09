#!/usr/bin/env python3
from tempfile import TemporaryDirectory

import yaml
from git import Repo

with open("git_sync.yml", "r", encoding="utf-8") as stream:
  try:
    _yaml = yaml.safe_load(stream)
  except yaml.YAMLError as exc:
    print(exc)

for _elem  in _yaml["pull"]:
  for _git,_push_targets in _elem.items():
    with TemporaryDirectory() as _tmp_dir:
      print("========================================")
      print("Start cloning {0}".format(_git))
      # Clone git repository
      repo = Repo.clone_from(_git, _tmp_dir, multi_options=["--bare", "--mirror"])
      print("Cloned {0} into {1} as bare".format(_git, _tmp_dir))
      _count = 0
      for _push_target in _push_targets:
        _count += 1
        remote = repo.create_remote("remote"+str(_count), _push_target)
        print("Pushing {0} to {1}".format(_git, _push_target))
        remote.push(all=True)
      print("========================================")
