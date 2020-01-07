from PIL import Image, ImageDraw

imageName = input('Введите путь к изображению: ')

image = Image.open(imageName)
draw = ImageDraw.Draw(image)
width = image.size[0]
height = image.size[1]
pix = image.load()
textImg = []

for i in range(width):
	for j in range(height):
		textImg.append('#%02x%02x%02x' % pix[i, j])

textFile = open(imageName + '.txt', 'w')
textFile.write(str(textImg))
textFile.close()