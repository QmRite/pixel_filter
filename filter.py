from PIL import Image
import numpy as np
import doctest


def count_mean_color(block_size):
    """
     Вычисляет средный оттенок блока заданного размера
     :param block_size: размер блока
     :return: cредний оттенок

    >>> count_mean_color(1)
    300
    >>> count_mean_color(10)
    300
    >>> count_mean_color(15)
    133
    >>> count_mean_color(-1)
    0
    """
    color_sum = np.sum(pixels[i: i + block_size, j: j + block_size])
    return int(color_sum // (block_size * block_size))


def generate_black_and_white_elem(block_size, block_color, grayscale):
    """
     Перекрашивает блок в черно-белые оттенки
     :param block_size: размер блока
     :param block_color: средний цвет блока
     :param grayscale: кол-во градаций серого
    """
    medium_color = int(block_color // grayscale) * grayscale / 3
    pixels[i: i + block_size, j: j + block_size] = medium_color


img = Image.open(input('Введите названия исходного изображения: '))
block_size = int(input("Введите размер блока: "))
grayscale = 255 // int(input("Введите шаг градаций серого: "))
pixels = np.array(img)
height = len(pixels)
width = len(pixels[1])

for i in range(0, height, block_size):
    for j in range(0, width, block_size):
        block_color = count_mean_color(block_size)
        generate_black_and_white_elem(block_size, block_color, grayscale)
res = Image.fromarray(pixels)

res.save(input("Введите название обработанного изображения: "))
