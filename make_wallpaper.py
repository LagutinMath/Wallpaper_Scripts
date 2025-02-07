from PIL import Image, ImageDraw, ImageFont
import ctypes
import os

BACKGROUND_COLOR, TEXT_COLOR = "#111111", "#CCCCCC"
IMG_WIDTH, IMG_HEIGHT = 2560, 1440
FONT_SIZE = 36
FONT_PATH = r"C:\Windows\Fonts\consola.ttf"
PADDING_X, PADDING_Y, LINE_SPACING = 500, 150, 10

image = Image.new("RGB", (IMG_WIDTH, IMG_HEIGHT), BACKGROUND_COLOR)
draw = ImageDraw.Draw(image)
font = ImageFont.truetype(FONT_PATH, FONT_SIZE)

with open("make_wallpaper.py", "r", encoding="utf-8") as f:
    lines = f.readlines()

y = PADDING_Y
for line in lines:
    draw.text((PADDING_X, y), line, font=font, fill=TEXT_COLOR)
    bbox = draw.textbbox((PADDING_X, y), line, font=font)
    text_height = bbox[3] - bbox[1]
    y += text_height + LINE_SPACING

image.save("wallpaper.png")
ctypes.windll.user32.SystemParametersInfoW(20, 0, os.path.abspath("wallpaper.png"), 0x01 | 0x02)
