import random

number = int(input("Введи число от 1 до 100 -"))
count = int(input("За сколько попыток ты хочешь выйграть?"))
number_2 = random.randint(1, 100)
while number != number_2:
    if count <= 0:
        print("Ты проиграл!")
        break
    if number > 100:
        print("Введи число от 1 до 100\nПожалуйста пжпжпжпжпжпжпж")
    elif number < number_2:
        print("Введи число больше!")
    elif number > number_2:
        print("Введи число меньше!")
    number = int(input("-"))
    count -= 1
else:
    print("Ты победил!")
