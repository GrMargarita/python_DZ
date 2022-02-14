"""2.Напишите программу Python, которая принимает слово от пользователя и переворачивает его """
# word = input("Input a word to reverse: ")
# for char in range(len(word) - 1, -1, -1):
#   print(word[char], end="")
# print()
"""3.Напишите программу Python для построения следующего шаблона, используя вложенный цикл for.
 * 
 * * 
 * * * 
 * * * * 
 * * * * * 
 * * * * 
 * * * 
 * * 
 *
 """
# width = int(input("width: "))
# for i in range(width):
#     for j in range(i):
#         print('* ', end="")
#     print('')
# for i in range(width, 0, -1):
#     for j in range(i):
#         print('* ', end="")
#     print('')

"""4.Даны два целых числа A и В. Выведите все числа от A до B включительно, в порядке возрастания, 
если A < B, или в порядке убывания если A > B"""

# a = int(input("A: "))
# b = int(input("B: "))
# z = 0
# for i in range(max(a, b) - min(a, b) + 1):
#     if a < b:
#         print(a + z)
#     else:
#         print(a - z)
#     z += 1

"""5. Даны два целых числа A и B (при этом A < B). Выведите все числа от A до B включительно."""

# A = int(input("A:"))
# B = int(input("B:"))
# print(*range(A, B+1))

"""6. Напишите программу, которая удаляет дубликаты элементов из списка."""
# li = []
# n = int(input("Enter size of list "))
# for x in range(0, n):
#     element = int(input("Enter element of list " + str(x + 1) + ":"))
#     li.append(element)
# b = set()
# unique = []
# for x in li:
#     if x not in b:
#         unique.append(x)
#         b.add(x)
# print("Non-duplicate items:")
# print(unique)

"""7.Напишите программу, которая копирует список"""

# li = []
# n = int(input("Enter size of list "))
# for x in range(0, n):
#     element = int(input("Enter element of list "))
#     li.append(element)
# print("Original list: ", li)
# # cloning
# list_copy = li[:]
# print("After cloning: ", list_copy)

"""8.Напишите программу, которая находит разницу между двумя списками и сохраняет ее в новый список. Вывести результат на экран."""

# list1_size = int(input("Enter size of list1 "))
# list1 = [int(input()) for i in range(list1_size)]
# print(list1)
# list2_size = int(input("Enter size of list2 "))
# list2 = [int(input()) for i in range(list2_size)]
# print(list2)
# difference = set(list1).symmetric_difference(set(list2))
# print(difference)

"""9.Напишите программу для объединения следующих словарей для создания нового"""

# dic1 = {1: 10, 2: 20}
# dic2 = {3: 30, 4: 40}
# dic3 = {5: 50, 6: 60}
# dic4 = {}
# for d in (dic1, dic2, dic3): dic4.update(d)
# print(dic4)

"""10."""
# d = dict()
# for x in range(1, 16):
#     d[x] = x ** 2
# print(d)
