from PIL import Image
import os
from pathlib import Path

for i in range(-1, 3):
    mypath = f"/Users/jonathankhanlian/PycharmProjects/web-game/img/transition/level_{i}/"

    for file in os.listdir(mypath):
        if file.endswith(".png"):
            file_name = Path(mypath + file).stem
            img = Image.open(mypath + file)
            rgb_im = img.convert("RGB")
            rgb_im.save(mypath + file_name + ".jpg")
