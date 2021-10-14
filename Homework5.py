# # Импортировал библиотеку Рандома.
# import random
# # Приветствие участника
# print("Добро пожаловать в игру Камень, Ножницы и Бумага")
# print("1 = Камень   2 = Ножницы    3 = Бумага")
# # Компьютер загадал число от 1 до 3 с помощью random.randint().
# computer = random.randint(1, 3)
# # Попросил ввести выбор участника.
# answer = int(input("Введи ответ - "))
# # Условие
# if answer == computer:
#     print("Ничья")
#     print("Ничего страшного")
# elif answer == 1:
#     if computer == 2:
#         print("Вы победили!")
#         print("Камень бьет ножницы!")
#     else:
#         print("Вы проиграли.")
#         print("Бумага оборачивает камень!")
# elif answer == 2:
#     if computer == 3:
#         print("Вы победили!")
#         print("Ножницы режут бумагу!")
#     else:
#         print("Вы проиграли.")
#         print("Камень бьет ножницы!")
# elif answer == 3:
#     if computer == 1:
#         print("Вы победили!")
#         print("Бумага оборачивает камень!")
#     else:
#         print("Вы проиграли.")
#         print("Ножницы режут бумагу!")
# elif answer > 3:
#     print("Не промахивайся по клавиатуре!!!")
# else:
#     print("Вы проиграли!")

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if abs(x1 - x2) == abs(y1 - y2):
    print('YES')
else:
    print('NO')