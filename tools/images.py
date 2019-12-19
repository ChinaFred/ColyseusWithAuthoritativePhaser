from PIL import Image, ImageDraw, ImageFont


def draw_fake_image(filepath):
    img = Image.new('RGB', (100, 100), color=(73, 109, 137))
    d = ImageDraw.Draw(img)
    d.text((18, 47), "Hello World", fill=(255, 255, 0))
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


