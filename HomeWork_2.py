a = input("Какой цвет ты предпочитаешь 'красный', 'синий', 'черный' или 'оранжевый'? -")
b = input("Кто ваш любимый автор 'Пушкин', 'Лермонтов', 'Некрасов' или 'Гоголь'? -")
c = input("Что вы больше любите: телефон, телевизор или компьютер -")
d = input("Что вы любите с утра чай, кофе или вода -")

if a == "красный" and b == "Лермонтов" and c == "телефон" and d == "чай":
    print("Вы очень похожи на меня!")
elif a == "красный" and b == "Пушкин" and c == "телевизор" and d == "кофе":
    print("Вы крутой! Я тоже люблю Пушкина.")
elif a == "синий" and b == "Некрасов" and c == "телефон" and d == "чай":
    print("Ты веселый, заводной и чудесный!")
elif a == "синий" and b == "Пушкин" and c == "компьютер" and d == "вода":
    print("Превосходно! Молодец!")
elif a == "черный" and b == "Гоголь" and c == "телефон" and d == "чай":
    print("Ты супер!")
elif a == "черный" and b == "Некрасов" and c == "компьютер" and d == "вода":
    print("Потресающе! Супер!")
elif a == "оранжевый" and b == "Лермонтов" and c == "компьютер" and d == "вода":
    print("Вы обладаете незаурядным умом!")
elif a == "оранжевый" and b == "Гоголь" and c == "телевизор" and d == "кофе":
    print("Excelent! You did it!")
else:
    print("Ошибка, завершаю работу!")