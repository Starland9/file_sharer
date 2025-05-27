from app.config import STYLE_PATH


def get_style():
    with open(STYLE_PATH) as f:
        style = f.read()
    return style
