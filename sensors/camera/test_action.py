from PIL import Image, ImageDraw
from robot import config


def test_draw_image(filename):
    img = Image.new('RGB', (100, 100), color=(73, 109, 137))
    d = ImageDraw.Draw(img)
    d.text((10, 10), "Hello World", fill=(255, 255, 0))
     img.save(config.current.writePicturePath + filename)
    config.current.set_lastPicture(filename)
    print(config.current.lastPicture)
