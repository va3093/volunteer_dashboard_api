import yaml

CONFIG_PATH = "./config.yml"
config = {}

with open(CONFIG_PATH, 'r') as f:
    config = yaml.load(f)
