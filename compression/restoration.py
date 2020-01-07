from PIL import Image, ImageDraw

fileName = input('Введите путь к файлу: ')

textFile = open(fileName + '.txt', 'r')
textImg = textFile.read()
textFile.close()

image = Image.open(imageName)
draw = ImageDraw.Draw(image)
width = image.size[0]
height = image.size[1]
pix = image.load()
 = []

for i in range(width):
	for j in range(height):
		textImg.append(pix[i, j])

