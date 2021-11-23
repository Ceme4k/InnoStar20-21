# a = list(map(int, input().split()))
# b = 0
# for i in range(len(a)):
#     for j in range(i + 1, len(a)):
#         if a[j] == a[i]:
#             b += 1
# print(b)

# a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# # Должен получить на экране:
# # 1 2 3
# # 4 5 6
# # 7 8 9
#
# # Вариант 1
# for i in range(len(a)): # i + 1 - номер строки
#     for j in range(len(a[i])): # j + 1 - номер столбца
#         print(a[i][j], end=" ")
#     print()
#
# # Вариант 2
# for i in a:
#     for j in i:
#         print(j, end=" ")
#     print()
#
# # Вариант 3
# for i in a:
#     print(*i)


# # 3 4 - количество строк и столбцов
# # 1 2 3 4
# # 5 6 7 8
# # 9 10 11 12
#
# # n - количество строк
# # m - количество стобцов
# n, m = map(int, input().split())
# a = []
# for i in range(n):
#     a.append(list(map(int, input().split())))
# print(a)


# n, m = map(int, input().split())
# # a = ([0] * m) * n - нельзя!
# a = []
# for i in range(n):
#     a.append([0]*m)
#
# print(a)
