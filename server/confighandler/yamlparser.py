"""This class is used to safely load configuration files written in yaml"""
import yaml as yaml


def load_config(config_file):
    """Use safe load to get the parameters from a yaml-file"""
    with open(config_file, 'r') as yaml_file:
        try:
            return yaml.safe_load(yaml_file)
        except yaml.YAMLError as exc:
            print(exc)