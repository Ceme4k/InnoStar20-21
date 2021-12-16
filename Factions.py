# def my_sum(*a):
#     sum_ = []
#     for i in a:
#         if -5 <= i or i <= 5:
#             sum_.append(i * i)
#         elif i > 5:
#             sum_.append(2 * i)
#         else:
#             sum_.append((2 * abs(i)) - 1)
#     return sum_
#
#
# a, b = map(int, input().split())
# print(my_sum(a))

# def square(x):
#     return x * x
#
#
# def two_by_x(x):
#     return 2 * x
#
#
# def module_by_2_min_1(x):
#     return 2 * abs(x) - 1
#
#
# def logic(a, b):
#     c = list(range(a, b + 1))
#     res = []
#     for x in c:
#         if -5 <= x <= 5:
#             res.append(square(x))
#         elif x > 5:
#             res.append(two_by_x(x))
#         else:
#             res.append(module_by_2_min_1(x))
#     return res
#
#
# a, b = map(int, input().split())
# res = logic(a, b)
# print(*res)


# def my_sum(*a):
#     sum_ = 0
#     for i in list(a[0]):
#         sum_ += i
#     return sum_
#
#
# def compute_average(*a):
#     c = my_sum(a) / 2
#     return c
#
#
# # a, b = map(int, input().split())
# print(compute_average(1, 2))


# a, b = map(int, input().split())
# c = list(range(a, b + 1))
# res = []
# for x in c:
#     if -5 <= x <= 5:
#         res.append(x * x)
#     elif x > 5:
#         res.append(2 * x)
#     else:
#         res.append(2 * abs(x) - 1)
# print(*res)

# a = int("BA", 16)
# print(a)


def a(a, b):
    c = int(str(a), int(b))
    return c


def t(a, b):
    n = []
    while int(a) / int(b):
        n.append(int(a) % int(b))
        a = int(a) // int(b)
    return n


z = input()
x = int(input())

if x > 10:
    print(a(z, x))
else:
    o = t(z, x)
p = reversed(o)
print(*p, sep="")




a = int(input())
sistema = int(input())
d = []
while a != 0:
    oi = a % sistema
    a = a // sistema
    d.append(oi)
d.reverse()
print(*d)


