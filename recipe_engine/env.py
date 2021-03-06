# Copyright 2016 The LUCI Authors. All rights reserved.
# Use of this source code is governed under the Apache License, Version 2.0
# that can be found in the LICENSE file.

"""Sets up recipe engine Python environment."""

import contextlib
import os
import sys

# Hook up our third party vendored packages.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
THIRD_PARTY = os.path.join(BASE_DIR, 'recipe_engine', 'third_party')

# USING_BOOTSTRAP is true if we're using the Python bootstrap. In this case,
# we will be running in a complete VirtualEnv, and will not need to have any
# funky path manipulations.
BOOTSTRAP_ENV_KEY = 'RECIPES_RUN_BOOTSTRAP'
USING_BOOTSTRAP = os.environ.pop(BOOTSTRAP_ENV_KEY, None)


# Install local imports.
sys.path = [
    THIRD_PARTY,
    os.path.join(THIRD_PARTY, 'client-py')
] + sys.path


@contextlib.contextmanager
def temp_sys_path():
  orig_path = sys.path[:]
  try:
    yield
  finally:
    sys.path = orig_path


if not USING_BOOTSTRAP:
  # Real path manipulation.
  sys.path = [
      os.path.join(THIRD_PARTY, 'requests'),
      os.path.join(THIRD_PARTY, 'six'),
      os.path.join(THIRD_PARTY, 'mock-1.0.1'),
      os.path.join(THIRD_PARTY, 'astunparse'),
  ] + sys.path

  # Hack up our "pkg_resources" to import our local protobuf instead of the
  # system one.
  #
  # As per https://github.com/google/protobuf/issues/1484:
  # The protobuf library is meant to be installed. It is either a system library
  # or a virtualenv library, but not something you can just point "sys.path" to
  # anymore ... well, not without hacks.
  #
  # Ideally we'd run recipe engine in its own virtualenv and make this happen.
  # In the meantime, we will go through the following ritual to ensure that our
  # protobuf package is preferred.
  #
  # We need to:
  # a) Load pkg_resources from third_party.
  # b) Ensure that our protobuf is the only element in sys.path. This causes it
  #    to cache it as the only option, rather than preferring the system
  #    library.
  # c) Build our standard first-is-preferred path for the remainder of the
  #    engine.
  import pkg_resources
  with temp_sys_path():
    # In a temporary environment where "sys.path" consists solely of our
    # "third_party" directory, register the google namespace. By restricting the
    # options in "sys.path", "pkg_resources" will not cache or prefer system
    # resources for this namespace or its derivatives.
    sys.path = [THIRD_PARTY]

    # Remove module if there is preloaded 'google' module
    sys.modules.pop('google', None)

    pkg_resources.declare_namespace('google')
    pkg_resources.fixup_namespace_packages(THIRD_PARTY)

  # From here on out, we're back to normal imports. Let's assert that the we're
  # using the correct protobuf package, though.
  #
  # We use "realpath" here because the importer may resolve the path differently
  # based on symlinks, and we want to make sure our calculated path matches the
  # impoter's path regardless.
  import google.protobuf
  assert (os.path.realpath(THIRD_PARTY) in
          os.path.realpath(google.protobuf.__path__[0]))

# Prune all VirtualEnv paths out of $PATH. This means that recipe engine
# 'unwraps' vpython VirtualEnv path manipulation. Invocations of `python` from
# recipes should never inherit the recipe engine's own VirtualEnv.
def _prune_virtualenvs(env):
  # Look for "activate_this.py" in this path, which is installed by VirtualEnv.
  # This mechanism is used by vpython as well to sanitize VirtualEnvs from
  # $PATH.
  env['PATH'] = os.pathsep.join([
    p for p in env.get('PATH', '').split(os.pathsep)
    if not os.path.isfile(os.path.join(p, 'activate_this.py'))
  ])

_prune_virtualenvs(os.environ)
