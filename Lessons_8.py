# a = int(input())
# d = int(input())
# b = a
# g = d
# c = 0
# while a != 0 or d != 0:
#     a = int(input())
#     d = int(input())
#     if a > b:
#         b = a
#         c = 0
#     if d > g:
#         c = 0
#     if a == b and d == g:
#         c += 1
# print(c)

# for i in range(2):
#     for y in range(2):
#         for r in range(2):
#             for e in range(2):
#                 print(i, y, r, e)

n = int(input()) * 1000
k = int(input())
c = 0
c1 = 0
while n != 1499:
    n -= 1500
    c += 1
    while k != 299:
        k -= 300
        c1 += 1
print(c1, c)
