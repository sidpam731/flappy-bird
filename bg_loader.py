from PIL import Image
import pygame as pg

def extract_gif_frames(path, total_frames=None):
    gif = Image.open(path)
    frames = []
    prev_frame = gif.convert("RGBA")  # first frame
    frames.append(prev_frame.copy())
    count = 1

    while not(total_frames and count >= total_frames):
        try:
            gif.seek(gif.tell() + 1)
            frame = gif.convert("RGBA")
            # composite onto previous frame
            combined = Image.alpha_composite(prev_frame, frame)
            frames.append(combined)
            prev_frame = combined
            count += 1
        except EOFError:
            break

    return frames


def surface_converter(frames):
    surfaces = []
    for frame in frames:
        converted = pg.image.fromstring(frame.tobytes(), frame.size, frame.mode)
        surfaces.append(converted)
    return surfaces

