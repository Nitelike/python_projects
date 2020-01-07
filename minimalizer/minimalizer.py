file_name = input('Enter file name: ')
dot = file_name.index('.')
file_name_min = file_name[: dot] + '-min' + file_name[dot :]
ext = file_name[dot + 1:]
min_text = ''

with open(file_name, 'r') as source:
	text = []

	if ext == 'cpp':
		for line in source:
			for i in range(0, len(line)):
				if line[i] == '\n' and line[i - 1] == ' ' and line[i - 2].isalpha():
					text.append('  ')
				elif line[i] != '\n' or (line[i] == '\n' and line[0] == '#') or line[i - 1].isalpha():
					text.append(line[i])

		for i in range(0, len(text)):
			if text[i] != ' ' or (text[i] == ' ' and (text[i - 1].isalpha() or text[i - 1].isnumeric()) and (text[i + 1].isalpha() or text[i + 1].isnumeric())):
				min_text += text[i]

with open(file_name_min, 'w') as output:
	output.write(min_text)

print('\nMinimalized successfully!\nSaved as: ' + file_name_min)