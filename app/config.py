import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONFIG_PATH = os.path.join(BASE_DIR, 'config.json')

STYLE_PATH = os.path.join(BASE_DIR, "app", "style", "style.qss")