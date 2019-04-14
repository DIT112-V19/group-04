"""Load the config file into the module"""

from os import path
from server.confighandler import yamlparser
import platform

module_dir = path.dirname(__file__)     # <-- absolute directory of the module
config_name = "config.yaml"             # name of the internal config-file
config_file_path = path.join(module_dir, config_name)
module_config = yamlparser.load_config(config_file_path)

host_pc = platform.node()