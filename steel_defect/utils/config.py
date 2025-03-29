import yaml
from pathlib import Path

def load_config(config_path):
    with open(config_path) as f:
        config = yaml.safe_load(f)
    return config

def save_config(config, config_path):
    with open(config_path, 'w') as f:
        yaml.dump(config, f)