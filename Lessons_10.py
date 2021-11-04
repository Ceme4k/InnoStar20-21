# a = input()
# c = ""
# for i in range(len(a)):
#     if a[i] != " ":
#         c += a[i]
# a = c
# c = a[::-1]
# if a == c:
#     print("yes")
# else:
#     print("no")


# a = input()
# for i in a:
#     if a.count(i) == 2:
#         print(i)
#         break
#
# a = input()
# while True:
#     if a.count(a) == 2:
#         print(a)
#         break

a = input()
for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if a[i] == a[j]:
            print(a[i])
