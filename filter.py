from PIL import Image
import numpy as np


def count_mosaic_color():
    color_sum = np.sum(pixels[i: i + mosaic_size, j: j + mosaic_size])
    return int(color_sum // (mosaic_size * mosaic_size))


def generate_black_and_white_elem():
    medium_color = int(elem_color // grayscale) * grayscale / 3
    pixels[i: i + mosaic_size, j: j + mosaic_size] = medium_color


print('Введите названия исходного изображения и результата через пробел')
inp_name, out_name = input().split()
img = Image.open(inp_name)
pixels = np.array(img)
height = len(pixels)
width = len(pixels[1])
mosaic_size = 10
grayscale = 50

for i in range(0, height, mosaic_size):
    for j in range(0, width, mosaic_size):
        elem_color = count_mosaic_color()
        generate_black_and_white_elem()
res = Image.fromarray(pixels)
res.save(out_name)
