from slurm_api_cli_proxy.command_handler import SbatchEvaluator

def test_sbatch_evaluator_ensure_default_working_dir():

  cli_args_dict: dict[str, str] = {}
  # no chdir or 'D' specified:


  sbatch_evaluator = SbatchEvaluator()
  sbatch_evaluator.ensure_default_working_dir("slurm_user_name", cli_args_dict)

  assert 'chdir' in cli_args_dict, "cli_args_dict should contain a 'chdir' value."
  assert cli_args_dict['chdir'] == "/home/slurm_user_name/", "cli_args_dict should contain the default home dir of the HPC user."

def test_sbatch_evaluator_preserve_explicit_chdir_key():

  cli_args_dict: dict[str, str]  = {}
  cli_args_dict['chdir'] = "/some/other/path/explicitly/given/"

  sbatch_evaluator = SbatchEvaluator()
  sbatch_evaluator.ensure_default_working_dir("slurm_user_name", cli_args_dict)

  assert 'chdir' in cli_args_dict, "cli_args_dict should contain a 'chdir' value."
  assert cli_args_dict['chdir'] == "/some/other/path/explicitly/given/", "cli_args_dict should contain the explicitly given working dir."

def test_sbatch_evaluator_preserve_explicit_d_key():

  cli_args_dict: dict[str, str]  = {}
  cli_args_dict['D'] = "/some/other/path/explicitly/given/"

  sbatch_evaluator = SbatchEvaluator()
  sbatch_evaluator.ensure_default_working_dir("slurm_user_name", cli_args_dict)

  assert 'D' not in cli_args_dict, "D should not be a key in cli_args_dict, anymore"
  assert 'chdir' in cli_args_dict, "cli_args_dict should contain a 'chdir' key."
  assert cli_args_dict['chdir'] == "/some/other/path/explicitly/given/", "cli_args_dict should contain the explicitly given working dir."
