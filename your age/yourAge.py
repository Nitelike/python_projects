#packages
import time

#main cycle
while True:
    #user input
    dateOfBirth = input('Введите дату вашего рождения (yyyymmdd): ')

    #current date
    dateNow = time.strftime('%Y%m%d')

    #variables
    years = []
    yearsNum = 0
    months = 0
    days = 0
    daysInMonth = 31

    #processing input data
    if dateOfBirth == 'break':
        break

    #amount of days in each month considering the leap year
    if int(dateOfBirth[4:6]) == 4 or int(dateOfBirth[4:6]) == 6 or int(dateOfBirth[4:6]) == 9 or int(dateOfBirth[4:6]) == 11:
        daysInMonth = 30
    elif int(dateOfBirth[4:6]) == 2:
        if int(dateOfBirth[0:4]) % 4 == 0:
            if int(dateOfBirth[4:6]) % 100 == 0:
                if int(dateOfBirth[4:6]) % 400 == 0:
                    daysInMonth = 29
        else:
            daysInMonth = 28

    #key variable, should be positioned before checking user input
    delta = str(int(dateNow) - int(dateOfBirth))

    #fill array with data
    for i in range(len(delta)):
        years.append(delta[i])

    while len(years) < 6:
        years.insert(0, '0')

    #calculate data
    yearsNum = int(years[0] + years[1])

    if int(years[2] + years[3]) > 12:
        months = 12 - (100 - int(years[2] + years[3]))
    else :
        months = int(years[2] + years[3])

    days = int(time.strftime('%d')) + (daysInMonth - int(dateOfBirth[6:8]) - 1)

    #output results
    print('Вам {0} лет, {1} месяцев и {2} дней'.format(yearsNum, months, days))
