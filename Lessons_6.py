# a = -1
# while a < 10:
#     a += 1
#     print(a)
#
# a = 11
# while a > 0:
#     a -= 1
#     print(a)
#
# a = 0
# while a < 40:
#     a += 2
#     print(a)
#

# for i in range(0, 11):
#     print(i)
#
# for x in range(10, -1, -1):
#     print(x)
#
# for z in range(2, 42, 2):
#     print(z)


a = int(input())
b = int(input())
c = int(input())
d = int(input())

for i in range(a, b+1):
    if (i % d) == c:
        print (i)