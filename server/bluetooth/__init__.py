# Loads the config file into the module and defines some module-level variables

from yaml import safe_load, YAMLError
from os import path
import platform


def load_config(config_file):
    with open(config_file, 'r') as yaml_file:
        try:
            return safe_load(yaml_file)
        except YAMLError as exc:
            print(exc)


module_dir = path.dirname(__file__)                  # absolute directory of the module
config_filename = "config.yaml"                      # name of the internal config-file
config_path = path.join(module_dir, config_filename)
module_config = load_config(config_path)
host_pc = platform.node()
