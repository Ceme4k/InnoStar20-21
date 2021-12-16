# def c(n):
#     if n / 10 < 1:
#         return 1
#     else:
#         return 1 + c(n // 10)
#
#
# a = int(input())
# print(c(a))


def c(n):
    v = n
    if n[::-1] == v:
        print("yes")
    else:
        print("no")


print(c(input()))




