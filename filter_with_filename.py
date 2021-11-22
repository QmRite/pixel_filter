from PIL import Image
import numpy as np


def count_elem_color():
    color_sum = np.sum(pixels[i: i + block_size, j: j + block_size])
    return int(color_sum // (block_size * block_size))


def generate_black_and_white_elem():
    medium_color = int(elem_color // grayscale) * grayscale / 3
    pixels[i: i + block_size, j: j + block_size] = medium_color


img = Image.open("img2.jpg")
block_size = 10
grayscale = 50
pixels = np.array(img)
height = len(pixels)
width = len(pixels[1])

for i in range(0, height, block_size):
    for j in range(0, width, block_size):
        elem_color = count_elem_color()
        generate_black_and_white_elem()
res = Image.fromarray(pixels)

res.save('res.jpg')