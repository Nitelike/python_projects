import base64

name = input('Введи путь к изображению: ')
strImg = ''

with open(name, 'rb') as imageFile:
	strImg = base64.b64encode(imageFile.read())

with open(name + '.tx', 'w') as textImageFile:
	textImageFile.write(str(strImg))