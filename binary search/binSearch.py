import time

startTime = time.time()

myList = []
size = int(input('Введите размер создаваемого списка: '))
element = int(input('Введите элемент списка: '))

for i in range(size):
    myList.append(i)

print('Список заполнен')

def binSearch(mylist, element):
    low = 0
    high = len(mylist) - 1

    while low <= high:
        mid = (high + low) // 2

        if mylist[mid] < element:
            low = mid + 1
        elif mylist[mid] > element:
            high = mid - 1
        else:
            return mid

    return None

print(binSearch(myList, element))

print(time.time() - startTime)
