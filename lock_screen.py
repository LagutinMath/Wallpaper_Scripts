from PIL import Image, ImageDraw
import numpy as np

IMG_WIDTH, IMG_HEIGHT = 2560, 1440
BACKGROUND_COLOR = "#111111"
CIRCLE_COLOR, CIRCLE_THICKNESS = "#CCCCCC", 6
CIRCLE_CENTRE = np.array([1280, 526])
START_CIRCLE_RADIUS = 150
SCALE = 6

circle_style = dict(
    xy=CIRCLE_CENTRE,
    outline=CIRCLE_COLOR,
    width=CIRCLE_THICKNESS
)


def scaled(dct):
    return {
        k: (v * SCALE if k not in {'outline'} else v)
        for k, v in dct.items()
    }


if __name__ == '__main__':
    img = Image.new("RGB", (SCALE * IMG_WIDTH, SCALE * IMG_HEIGHT), BACKGROUND_COLOR)
    draw = ImageDraw.Draw(img, "RGBA")

    for r in np.arange(start=START_CIRCLE_RADIUS, stop=IMG_WIDTH, step=250.):
        pars = {**circle_style, 'radius': int(r)}
        draw.circle(**scaled(pars))

    final_img = img.resize((IMG_WIDTH, IMG_HEIGHT), Image.LANCZOS)
    final_img.save("lock_screen.png")
