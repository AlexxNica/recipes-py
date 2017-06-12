# Copyright 2017 The LUCI Authors. All rights reserved.
# Use of this source code is governed under the Apache License, Version 2.0
# that can be found in the LICENSE file.

from recipe_engine import recipe_api

class GeneratorScriptApi(recipe_api.RecipeApi):
  def __call__(self, path_to_script, *args):
    """Run a script and generate the steps emitted by that script.

    The script will be invoked with --output-json /path/to/file.json. The script
    is expected to exit 0 and write steps into that file. Once the script
    outputs all of the steps to that file, the recipe will read the steps from
    that file and execute them in order. Any *args specified will be
    additionally passed to the script.

    The step data is formatted as a list of JSON objects. Each object
    corresponds to one step, and contains the following keys:
      name: the name of this step.

      cmd: a list of strings that indicate the command to run (e.g. argv)

      env: a {key:value} dictionary of the environment variables to override.
       every value is formatted with the current environment with the python
       % operator, so a value of "%(PATH)s:/some/other/path" would resolve to
       the current PATH value, concatenated with ":/some/other/path"

      cwd: an absolute path to the current working directory for this script.

      always_run: a bool which indicates that this step should run, even if
        some previous step failed.

      outputs_presentation_json: a bool which indicates that this step will emit
        a presentation json file. If this is True, the cmd will be extended with
        a `--presentation-json /path/to/file.json`. This file will be used to
        update the step's presentation on the build status page. The file will
        be expected to contain a single json object, with any of the following
        keys:
          logs: {logname: [lines]} specifies one or more auxillary logs.
          links: {link_name: link_content} to add extra links to the step.
          step_summary_text: A string to set as the step summary.
          step_text: A string to set as the step text.
          properties: {prop: value} build_properties to add to the build status
            page. Note that these are write-only: The only way to read them is
            via the status page. There is intentionally no mechanism to read
            them back from inside of the recipes.

      allow_subannotations: allow this step to emit legacy buildbot
        subannotations. If you don't know what this is, you shouldn't use it. If
        you know what it is, you also shouldn't use it.
    """
    f = '--output-json'
    step_name = 'gen step(%s)' % self.m.path.basename(path_to_script)

    with self.m.context(cwd=self.m.path['checkout']):
      if str(path_to_script).endswith('.py'):
        step_result = self.m.python(
          step_name,
          path_to_script, list(args) + [f, self.m.json.output()])
      else:
        step_result = self.m.step(
          step_name,
          [path_to_script,] + list(args) + [f, self.m.json.output()])
    new_steps = step_result.json.output
    assert isinstance(new_steps, list), new_steps

    failed_steps = []
    for step in new_steps:
      cmd = step['cmd']
      assert all(isinstance(arg, basestring) for arg in cmd), cmd

      outputs_json = step.pop('outputs_presentation_json', False)
      if outputs_json:
        # This step has requested a JSON file which the binary that
        # it invokes can write to, so provide it with one.
        cmd.extend(['--presentation-json', self.m.json.output(False)])

      if not failed_steps or step.get('always_run'):
        try:
          cwd = self.m.path.abs_to_path(step['cwd']) if 'cwd' in step else None
          with self.m.context(env=step.get('env'), cwd=cwd):
            self.m.step(
              step['name'], cmd,
              allow_subannotations=bool(step.get(
                'allow_subannotations', False)),
            )
        except self.m.step.StepFailure:
          failed_steps.append(step['name'])
        finally:
          step_result = self.m.step.active_result
          if outputs_json:
            p = step_result.presentation
            j = step_result.json.output

            if j:
              p.logs.update(j.get('logs', {}))
              p.links.update(j.get('links', {}))
              p.step_summary_text = j.get('step_summary_text', '')
              p.step_text = j.get('step_text', '')
              p.properties.update(j.get('properties', {}))

    if failed_steps:
      raise self.m.step.StepFailure(
        "the following steps in %s failed: %s" %
        (step_name, failed_steps))
