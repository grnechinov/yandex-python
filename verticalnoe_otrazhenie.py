from PIL import Image


def mirror():
    im = Image.open("image.jpg")
    pixels = im.load()
    x, y = im.size
    for i in range(0, x // 2):
        for j in range(0, y):
            pixels[i, j], pixels[x - i - 1, j], pixels[y - i - 1]\
                = pixels[x - i - 1, j], pixels[i, j], pixels[y - i - 1]
    im.save('res.jpg')
