ruble_and_penny = float(input("Введи стоимость пирожка - "))
pie = float(input("Введи количество пирожков - "))
print(int(ruble_and_penny * pie))


ruble = float(input("Введи стоимость пирожка(в рублях) - "))
penny = int(float(input("Введи стоимость пирожка(в копейках) - ")))
pie = float(input("Введи количество пирожков - "))
a = penny / 100
print(int((ruble + (penny / 100)) * pie))