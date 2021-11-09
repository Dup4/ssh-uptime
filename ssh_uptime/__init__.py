import yaml
import logging
from .config import config

config_path = './config.yaml'
with open(config_path, 'r') as f:
    default_config = config(yaml.load(f, Loader=yaml.FullLoader))

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

consoleHandler = logging.StreamHandler()
consoleHandler.setFormatter(logging.Formatter(
    '%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s'))

logger.addHandler(consoleHandler)
