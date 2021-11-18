# a = list(map(int, input().split()))
# b = 0
# c = 0
# d = 0
# for i in range(len(a)):
#     if a[i] > 0:
#         b += a[i]
#         c += 1
#     else:
#         d += 1
# print(b)
# print(c)
# print(d)


# a = list(map(int, input().split()))
# for i in range(1, len(a)):
#     if a[i] > a[i - 1]:
#         print(a[i])


# a = list(map(int, input().split()))
# b = 0
# for i in range(1, len(a)):
#     if a[i] > (a[i - 1] * 2):
#         b += 1
# print(b)

# a = list(map(int, input().split()))
# v = a.index(max(a))
# f = a.index(min(a))
# b = max(a)
# c = min(a)
# a[v], a[f] = a[f], a[v]
# print(*a)
