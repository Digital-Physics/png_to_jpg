from PIL import Image
import os
from pathlib import Path

for i in range(15):
    mypath = f"/Users/jonathankhanlian/PycharmProjects/web-game/img/movie_png_seq{i}/"

    for file in os.listdir(mypath):
        if file.endswith(".png"):
            file_name = Path(mypath + file).stem
            img = Image.open(mypath + file)
            img.save(mypath + file_name + ".jpg")
