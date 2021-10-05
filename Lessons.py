# x = True
# y = True
# z = True
# v = x or not(x and(y or not z))
# print(v)

# 1. not z = not True = False
# 2. y or not z = True or False = /1+0/ = True
# 3 x and () = True and True = /1*1/ = True
# 4 not() = not True = False
# 5 x or not() = True or False = /1+0/ = True

# & = and
# v = or
# -| = not

# a = x and y or not y
# print(a)

# print( 5 > 4 )
# print( 5 < 4 )
# print( 5 == 4 )
# print( 5 == 5 )
# print( 5 != 4 )
# print( 5 != 5 )
#
# result = 7 > 5
# print(result)

# is_rain = True
# is_rain = False
# is_rain = input("Идет Дождь? Да/Нет")
# if is_rain == "ДА" or is_rain == "да":
#     print("Возми зонт")
# else:
#     print("Возми кепку")
# print("Я вышел на улицу")
#
# a = int(input("Введи число - "))
# if a % 2 == 0:
#     print("Yes")
# else:
#     print("No")

# a = int(input("Введи число - "))
# b = int(input("Введи число - "))
#
# print(max(a,b))
#
# if a > b:
#     print(a)
# else:
#     print(b)

s = int(input("Введи год - "))
if (s % 4 == 0) and (s % 100 != 0) or (s % 400 == 0):
    print("Yes")
else:
    print("No")





