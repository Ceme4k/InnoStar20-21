# n = int(input())
# i = 1
# while i ** i <= n:
#     print(i ** 2)
#     i += 1

#
# n = int(input())
# i = 2
# while n % i != 0:
#     i += 1
# print(i)


# a = int(input())
# k = 0
# for i in range(0, a):
#     d = int(input())
#     k = k + d
#     if a < 0:
#         print("")
#         break
# else:
#     print(k)
#
#
#
#
# a = int(input())
# k = 0
# for i in range(a):
#     d = int(input())
#     k = k + d
# print(k)

# r = 1
# m = 0
# while True:
#     a = int(input())
#     if a > r:
#         r = a
#         m =
#     if a == 0:
#         break
# print(r)




a = int(input())
b = 0
c = 0
while a != 0:
    a = int(input())
    if a > b:
        b, c = a, 1
    elif a == b:
        c += 1
print(c)