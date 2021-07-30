from yaml import FullLoader
import yaml


def yaml_config(config_file_path):
    """Get the config from the configuration file"""
    with open(config_file_path, 'r') as file:
        config = yaml.load(file, Loader=FullLoader)
    return config['mysql']
