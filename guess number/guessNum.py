number = 45
running = True
attempts = 1

while running:
	userNumber = int(input("Угадайте целое число от 1 до 100 : "))

	if userNumber == number:
		print("Вы угадали число! Количество попыток :", attempts)
		running = False
	elif userNumber < number:
		print("Мало. Попробуйте еще :")
		attempts = attempts + 1
	else:
		print("Много. Попробуйте еще :")
		attempts = attempts + 1