# Упражнение №1
x = True
y = False
z = not(x or not(y and x))
print(z)

# 1. y and x = False and True = /0*1/ = False
# 2. not(y and x) = not False = True
# 3. x or not(y and x) = True or True = True
# 4. not(x or not(y and x)) = not True = False

# Упражнение №2
sign = int(input("Введи число - "))
if sign > 0:
    print(1)
elif sign < 0:
    print(-1)
else:
    print(0)

