from PIL import Image
import os
from pathlib import Path

# backup location
save_path = "/Users/jonathankhanlian/Desktop/original_pngs_of_digital_physics_video_game/"

for i in range(15):
    mypath = f"/Users/jonathankhanlian/PycharmProjects/web-game/img/movie_png_seq{i}/"

    for file in os.listdir(mypath):
        if file.endswith(".png"):
            file_name = Path(mypath + file).stem
            img = Image.open(mypath + file)
            rgb_im = img.convert("RGB")
            rgb_im.save(mypath + file_name + ".jpg", quality=100)

            # save it somewhere else just in case we want it again
            img.save(save_path + file)

            # delete .png after using it and (saving it somewhere else just in case)
            os.remove(mypath + file)
