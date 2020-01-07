phoneBook = {}
commands = ['стоп', 'добавить', 'удалить', 'просмотреть', 'поиск', 'изменить']

with open('phoneBook.txt', 'r') as file:
    text = file.read()
    if not text == '':
        phoneBook = eval(text)

while True:
    mode = input('\nВведите действие, которое хотите совершить: ')

    if mode == commands[0]:
        break

    elif mode == commands[1]:
        name = input('Введите имя контакта: ')
        number = int(input('Введите номер контакта: '))

        for nameInBook, numberInBook in phoneBook.items():
            if numberInBook == number or nameInBook == name:
                print('В телефонной книге уже есть контакт {0} с номером {1}'.format(nameInBook, numberInBook))
                break

        phoneBook.update({name : number})

        with open('phoneBook.txt', 'w') as file:
            file.write(str(phoneBook))

        print('Контакт успешно добавлен')

    elif mode == commands[2]:
        name = input('Введите имя контакта: ')
        phoneBook.pop(name)

        with open('phoneBook.txt', 'w') as file:
            file.write(str(phoneBook))

        print('Контакт успешно удален')

    elif mode == commands[3]:
        for nameInBook, numberInBook in phoneBook.items():
            print(nameInBook, numberInBook)

    elif mode == commands[4]:
        searchMode = input('Введите "имя", если поиск идет по имени\nВведите "номер", если поиск идет по номеру: ')
        searchData = ''
        find = False

        if searchMode == 'имя':
            searchData = input('Введите имя контакта: ')
        elif searchMode == 'номер':
            searchData = int(input('Введите номер контакта: '))
        else:
            print('Введены ошибочные параметры')
            break

        for nameInBook, numberInBook in phoneBook.items():
            if searchData == numberInBook or searchData == nameInBook:
                print(nameInBook, numberInBook)
                find = True

        if find == False:
            print('Контакт не найден')

    elif mode == commands[5]:
        name = input('Введите имя контакта: ')

        find = False

        for nameInBook, numberInBook in phoneBook.items():
            if name == nameInBook:
                find = True

        if find == False:
            print('Контакт с именем {0} в телефонной книге не найден'.format(name))

        changeMode = input('Введите "имя", если нужно изменить имя\nВведите "номер", если нужно изменить номер: ')

        if changeMode == 'имя':
            newName = input('Введите новое имя контакта: ')
            phoneBook[newName] = phoneBook.pop(name)

        elif changeMode == 'номер':
            newNumber = int(input('Введите новый номер контакта: '))
            phoneBook[name] = newNumber
        else:
            print('Введены ошибочные параметры')
            break

        with open('phoneBook.txt', 'w') as file:
            file.write(str(phoneBook))

        print('Контакт успешно изменен')

    else:
        print('\nНеправильная комманда, список доступных комманд:')

        for i in commands:
            print(i)
