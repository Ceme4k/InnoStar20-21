ruble_and_penny = float(input("Введи стоимость пирожка - "))
pie = float(input("Введи количество пирожков - "))
print(int(ruble_and_penny * pie))


ruble = float(input("Введи стоимость пирожка(в рублях) - "))
penny = float(input("Введи стоимость пирожка(в копейках) - "))
pie = float(input("Введи количество пирожков - "))
print(int((ruble + (penny / 100)) * pie))