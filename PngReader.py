from PIL import Image
import os


def getSomeBitmaps(count, directory):
    vectors = [[]] * count
    idx = 0
    for filename in os.listdir(directory):
        if idx == count:
            break
        im = Image.open(directory + '/' + filename)
        height = im.size[0]
        width = im.size[1]
        vectors[idx] = [1] * (height * width)
        pix = im.load()
        for i in range(height):
            for j in range(width):
                if pix[j, i][0] > 122:
                    vectors[idx][i * width + j] = -1
    return vectors
