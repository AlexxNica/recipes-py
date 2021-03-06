#!/usr/bin/env python
# Copyright 2016 The LUCI Authors. All rights reserved.
# Use of this source code is governed under the Apache License, Version 2.0
# that can be found in the LICENSE file.

import subprocess
import sys
import unittest

import repo_test_util


class RemoteTest(repo_test_util.RepoTest):
  def test_run(self):
    repos = self.repo_setup({'a': []})
    self.update_recipe_module(repos['a'], 'mod', {'foo': []})
    self.update_recipe(repos['a'], 'a_recipe', ['mod'], [('mod', 'foo')])
    try:
      subprocess.check_output([
          sys.executable, self._recipe_tool,
          '-v', '-v', 'remote',
          '--repository', repos['a']['root'],
          '--',
          'run',
          'a_recipe',
      ], stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as ex:
      print >> sys.stdout, ex.message, ex.output
      raise


if __name__ == '__main__':
  sys.exit(unittest.main())
