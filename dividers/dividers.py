while True:
    num = int(input('Enter a number: '))

    dividers = []

    for i in range(2, round(num/2)+1):
        if num % i == 0:
            dividers.append(i)

    print(*dividers)
