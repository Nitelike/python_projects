import os

char = input('Введи что-нибудь: ')
print()

stair = [char]

while (len(stair) * len(char)) + (1 * len(stair)) <= os.get_terminal_size()[0]:
    for i in stair:
        print(i, end = ' ')
    print()
    stair.append(char)
