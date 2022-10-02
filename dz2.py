# №2 Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример: N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
n = int(input('Введите число n '))
proizvedenie = 1
for i in range(1, n+1):
    proizvedenie *=i
    print(proizvedenie, end = ' ')


a = int(input("Введите число N: "))
i = 0
x = 0
lst = []
while i <= a - 1:
    i += 1
    b = (1 + (1 / i)) ** i
    lst.append(b)
    x = x + b
print("Список последовательных чисел числа N:", lst)
print("Сумма последовательных чисел числа N по формуле (1+ (1/n))^n равна", round(x, 2))

import math
# Линейный конгруэнтный метод

m=32768
a=23
b=12345
# a=a1+a10*10 # случайный выбор множителя (это мои пробы)
# можно еще попробовать случайно выбирать из массива рекомендованных констант

def lin_rand_arr_flxd(seed,size):
    if size==1:
        return math.ceil(math.fmod(a*math.ceil(seed)+b,m))
    r=[0 for i in range(size)]
    r[0]=math.ceil(seed)
    for i in range(1,size):
        r[i]=math.ceil(math.fmod((a*r[i-1]+b),m))
    return r[1:size]

arr5 = (lin_rand_arr_flxd(time.time(),len(lst5)+1))
print(arr5)

def selection_sort(arr_mix, arr):
    for i in range(len(arr)):
        minimum = i

        for j in range(i + 1, len(arr)):
            # Выбор наименьшего значения
            if arr[j] < arr[minimum]:
                minimum = j

        # Помещаем это перед отсортированным концом массива
        arr[minimum], arr[i] = arr[i], arr[minimum]
        arr_mix[minimum], arr_mix[i] = arr_mix[i], arr_mix[minimum]
        # здесь первичный массив сортируем вместе со случайным...

    return arr_mix


print(lst5)
print(selection_sort(lst5, arr5))



def myShuffle2(some_list):
    if len(some_list) >= 3:
        for i in range(0, len(some_list)-1):
            j = datetime.now().microsecond % len(some_list)-1  # текущее время в микросекундах
            some_list[i], some_list[j] = some_list[j], some_list[i]
    else:
        print("Нечего тут перемешивать")
        # some_list.reverse()
    return some_list
Бинарный сдвиг def myShuffle2(some_list):
    if len(some_list) >= 3:
        for i in range(0, len(some_list)-1):
            j = datetime.now().microsecond % 10 >> 2  # текущее время в микросекундах
            some_list[i], some_list[j] = some_list[j], some_list[i]
    else:
        print("Нечего тут перемешивать")
        # some_list.reverse()
    return some_list


# Проверка:
list1 = [10, -12, -13, 8]
