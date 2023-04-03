from pathlib import Path
from PIL import Image

path = Path("./docs/assets/colors")

colors = {
    "black": (40, 40, 40),
    "white": (237, 218, 176),
    "grey": (98, 100, 106),
    "blue": (64, 81, 181),
    "green": (104, 157, 105),
    "yellow": (215, 153, 34),
    "red": (201, 37, 29)
}

for color in colors:
    img_color  = Image.new(mode="RGB", size=(15, 15), color = colors.get(color))
    img_color.save(path.joinpath(f"{color}.png"))
