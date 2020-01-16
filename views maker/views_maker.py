import os
import time
import webbrowser

cycles = int(input("Введите количество циклов: "))
pages = int(input("Введите количество страниц, открываемых в каждом цикле: "))
delay = int(input("Введите задержку для каждого цикла: "))
url = input("Введите ссылку на страницу: ")

times = cycles * pages
print("Вы попадете на сайт " + url + " " , times, " раз")

for i in range(cycles):
	for j in range(pages):
		webbrowser.open(url)
	time.sleep(delay)
	os.system("taskkill /im chrome.exe /f")
	print("Цикл ", i + 1, " из ", cycles)