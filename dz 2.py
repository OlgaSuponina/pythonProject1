#Задача 2
# №2 Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример: N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
#n = int(input('Введите число n '))
#proizvedenie = 1
#for i in range(1, n+1):
 #   proizvedenie *=i
  #  print(proizvedenie, end = ' ')



# Задача 3
#a = int(input("Введите число N: "))
#i = 0
#x = 0
#lst = []
#while i <= a - 1:
 #   i += 1
  #  b = (1 + (1 / i)) ** i
   # lst.append(b)
    #x = x + b
#print("Список последовательных чисел числа N:", lst)
#print("Сумма последовательных чисел числа N по формуле (1+ (1/n))^n равна", round(x, 2))



# Задача 1
# Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.

# Пример:

# Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

#n = int(input('Введите натуральное число '))
#dict = {}
#for i in range (1,n+1):
 #    dict[i] = 3*i + 1
#print(dict)


# Задача 5
#Реализуйте алгоритм перемешивания списка.(Без использования библиотеки random)
#from time import time

#lister = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

#def mix_list(old: list) -> list:
 #   new = []
  #  while old:
  #      x = str(time()).split('.')[1]
  #      x = list(map(int, [x[0], x[-1]]))
  #      x = x[0] if x[0] <= x[1] else x[1]
  #      if x > len(old)-1:
  #          new.append(old.pop(0))
  #      else:
  #          new.append(old.pop(x))
  #  return new

#lister = mix_list(lister)
#print(lister)