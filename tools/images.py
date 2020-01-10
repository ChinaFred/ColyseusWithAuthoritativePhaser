# coding: utf-8
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime


def draw_fake_image(filepath):
    img = Image.new('RGB', (300, 200), color=(73, 109, 137))
    d = ImageDraw.Draw(img)
    d.text((110, 60), "Hello world", fill=(255, 255, 0))
    d.text((110, 90), datetime.now().strftime('%Y-%m-%d'), fill=(0, 255, 255))
    d.text((110, 120), datetime.now().strftime('%H:%M:%S'), fill=(125, 0, 125))
    img.save(filepath)


def draw_logo(filepath, name):
    img = Image.new('RGBA', (100, 100), (255, 0, 0, 0))
    d = ImageDraw.Draw(img)
    f = ImageFont.truetype("arial.ttf", 15)
    d.text((10, 10), name, font=f)
    f = ImageFont.truetype("arial.ttf", 15)
    d.text((10, 10), name, font=f, fill=(255, 255, 255))
    img.save(filepath, 'PNG')
    #marche pas faut downloader des font pour faire comme le logo du site initial


