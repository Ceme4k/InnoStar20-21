# var_None = None
# print(var_None, type(var_None))
# var_True = True
# print(var_True, type(var_True))
# var_False = False
# print(var_False, type(var_False))
# var_int = -6729384933784927
# print(var_int, type(var_int))
# var_float = -676293642949235e4
# print(var_float, type(var_float))
# var_complex = 0.39j + 7j
# print(var_complex, type(var_complex))
# var_str = "Hello my name is Roma!!!"
# print(var_str, type(var_str))

#
# number = int(input("Введи число:"))
# print(f"The next number for the number {number} is {number + 1}")
#
# print(f"The next number for the number {number} is {number - 1}")

# a = -4
# print(abs(a))
# b = 2.7
# c = 2.3
# print(round(b))
# print(round(c))
#
# print(max(a,b,c))
#
# print(min(a,b,c))
# a = pow(a,2)
# print(a)


# n = int(input("Сколько школьников - "))
# k = int(input("Сколько яблоков - "))
# print("Всем поравну по " + str(k//n) )
# print("Отаток " + str(k % n))

# a = int(input("Введи число - "))
# b = a//100
# x = a%100//10
# h = a%10
# print(b)
# print(x)
# print(h)

a = input()
b = input()

a,b=b,a
print(a,b)

m = a
a = b
b = m
print(a,b)


a = a + b
b = a - b
a = a - b
print(a,b)


