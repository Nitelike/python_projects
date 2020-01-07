#IMPORTING MODULES

import time
import random
import os
from PIL import Image, ImageDraw

#VARIABLES
counter = 0
defaultPathToResult = 'changedImages'

#USER INPUTS

pathToInitial = input('Введите путь к исходному файлу: ')

pathToResult = input('Введите путь к директории сохранения файла (без имени файла): ')

mode = input('Введите номер способа: ')

#PROCESSING USER INPUT

#processing extension and initial file path
if pathToInitial == '':
    files = []
    for folder_name, subfolders, filenames in os.walk('.'):
        for filename in filenames:
            file_path = os.path.join(folder_name, filename)
            files.append(file_path)

    for file in files:
       if file[len(file)-3 : len(file)] == 'jpg' or file[len(file)-3 : len(file)] == 'png':
            pathToInitial = file
            break

extension = pathToInitial[len(pathToInitial)-3 : len(pathToInitial)]

#processing path
if pathToResult == '':
    pathToResult = defaultPathToResult
    if not os.path.exists(pathToResult):
        os.mkdir(pathToResult)

name = pathToResult + os.sep + time.strftime('%Y%m%d%H%M%S')

#processing mode
if mode == '':
    mode = 0
else:
    mode = int(mode)

#USING PIL

image = Image.open(pathToInitial) #Открываем изображение.
draw = ImageDraw.Draw(image) #Создаем инструмент для рисования.
width = image.size[0] #Определяем ширину.
height = image.size[1] #Определяем высоту.
pix = image.load() #Выгружаем значения пикселей.

#FUNCTIONS

def fillArray(array, d1, d2, reverseWidthAndHeight = False):
    for i in range(d1):
        for j in range(d2):
            if reverseWidthAndHeight == False:
                array.append(pix[i, j])
            else:
                array.append(pix[j, i])

def fillRgboArrays(arrayR, arrayG, arrayB, arrayO, d1, d2):
    for i in range(d1):
        for j in range(d2):
            r = pix[i, j][0]
            g = pix[i, j][1]
            b = pix[i, j][2]

            if r > g and r > b:
                arrayR.append(pix[i, j])
            elif g > r and g > b:
                arrayG.append(pix[i, j])
            elif b > r and b > g:
                arrayB.append(pix[i, j])
            else:
                arrayO.append(pix[i, j])

def sort(*arrays):
    for array in arrays:
        array.sort()

def fillImageFrom(array, d1, d2):
    for i in range(d1):
        for j in range(d2):
            global counter
            if counter < len(array):
                draw.point((i, j), array[counter])
            counter += 1

#CHANGING IMAGES

if mode == 0:
    red = []
    green = []
    blue = []
    other = []

    fillRgboArrays(red, green, blue, other, width, height)
    sort(red, green, blue, other)
    final = red + green + blue + other
    fillImageFrom(final, width, height)
    name += '_mode0'

if mode == 1:
    red = []
    green = []
    blue = []
    other = []

    fillRgboArrays(red, green, blue, other, width, height)
    final = red + green + blue + other
    final.sort()
    fillImageFrom(final, width, height)
    name += '_mode1'

if mode == 2:
    final = []
    fillArray(final, width, height)
    random.shuffle(final)
    fillImageFrom(final, width, height)
    name += '_mode2'

if mode == 3:
    final = []
    fillArray(final, height, width, True)
    final.reverse()
    fillImageFrom(final, width, height)
    name += '_mode3'

if mode == 4:
    final = []
    fillArray(final, width, height)
    final.reverse()
    fillImageFrom(final, width, height)
    name += '_mode4'

if mode == 5:
    final = []
    for i in range(width):
        for j in range(height):
            r = pix[i, j][0]
            g = pix[i, j][1]
            b = pix[i, j][2]
            RGBint = (r<<16) + (g<<8) + b
            final.append(RGBint)

    final.sort()

    for i in final:
        blue =  i & 255
        green = (i >> 8) & 255
        red =   (i >> 16) & 255
        i = [red, green, blue]


    fillImageFrom(final, width, height)
    name += '_mode5'

if mode == 6:
    final = []
    for i in range(width):
        for j in range(height):
            r = pix[i, j][0] / 255
            g = pix[i, j][1] / 255
            b = pix[i, j][2] / 255
            rgb = (r, g, b)
            if max(rgb) == min(rgb):
                hue = 0
            elif max(rgb) == r:
                hue = (g-b)/(max(rgb)-min(rgb))
            elif max(rgb) == g:
                hue = 2 + (b-r)/(max(rgb)-min(rgb))
            elif max(rgb) == b:
                hue = 4.0 + (r-g)/(max(rgb)-min(rgb))

            final.append((hue, pix[i, j]))

    final.sort()
    for i in range(width):
        for j in range(height):
            if counter < len(final):
                draw.point((i, j), final[counter][1])
            counter += 1
    name += '_mode6'

#SAVING RESULTS

name +=  '.' + extension
image.save(name, 'PNG')
print('Сохранено в', name)
