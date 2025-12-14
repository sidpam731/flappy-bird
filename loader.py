import random,bg_loader
import pygame as pg
from types import SimpleNamespace

def load_assets(path="resources/"):


    # sounds
    sounds = {
        "point": pg.mixer.Sound(path + "point.ogg"),
        "hit": pg.mixer.Sound(path + "hit.ogg"),
        "death": pg.mixer.Sound(path + "die.ogg")
    }

    # backgrounds
    bg_frames = bg_loader.extract_gif_frames(path + "cycle.gif",40)
    bg_surfaces = bg_loader.surface_converter(bg_frames)
    backgrounds = {
        "day" : pg.image.load(path + "background-day.png"),
        "cycle" : bg_surfaces
    }



    #choose a color every time the app loads
    color = random.choice(["blue","red","yellow"])

    # bird frames
    down_flap = pg.image.load(path + f"{color}bird-down_flap.png")
    up_flap = pg.image.load(path + f"{color}bird-up_flap.png")
    chars = {
        "mid" : pg.image.load(path + f"{color}bird-mid_flap.png"),
        "down" : pg.transform.rotate(down_flap, 325),
        "up" : pg.transform.rotate(up_flap, 30)
    }

    # numbers (0-9)
    numbers = [pg.image.load(f"{path}{i}.png") for i in range(10)]
    # pipes
    # also choose a random pipe color

    l_pipe_img = pg.image.load(path + f"pipe-{random.choice(["red","green"])}.png")
    u_pipe_img = pg.transform.rotate(l_pipe_img, 180)

    pipes = {
        "lower": l_pipe_img,
        "upper": u_pipe_img
    }
    #exculcive
    icon = pg.image.load(path + "favicon.ico")
    base = pg.image.load(path + "base.png")
    game_over = pg.image.load(path + "game_over.png")


    # combine all assets in a dictionary
    assets = SimpleNamespace({
        "sounds": SimpleNamespace(**sounds),
        "backgrounds": SimpleNamespace(**backgrounds),
        "birds": SimpleNamespace(**chars),
        "pipes": SimpleNamespace(**pipes),
        "numbers": numbers,
        "icon": icon,
        "base": base,
        "game_over": game_over
    })

    return assets

def load_setting(path="config.txt"):
    data = {}
    with open(path) as f:
        for line in f:
            key, value = line.strip().split("=")
            if value.isdigit():
                data[key] = int(value)
            else:
                    data[key] = value

    return data