# Copyright 2015 The LUCI Authors. All rights reserved.
# Use of this source code is governed under the Apache License, Version 2.0
# that can be found in the LICENSE file.

from recipe_engine.recipe_api import Property, RequireClient
from recipe_engine import config

DEPS = [
    'properties',
]

PROPERTIES = {}

RETURN_SCHEMA = config.ReturnSchema(
    result=config.Single(int),
)

dependency_manager = RequireClient('dependency_manager')

def RunSteps(api):
  res = dependency_manager.depend_on(
      'engine_tests/depend_on/bottom', {'number': 'lalala'})

def GenTests(api):
  yield (
      api.test('basic') +
      api.properties() +
      api.expect_exception('TypeError')
  )
