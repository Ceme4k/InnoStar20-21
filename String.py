a = input()
b = a.replace(" ", "")
d = b.lower()
c = ""
l = ""
for i in d:
    if c.count(i) == 0:
        c += i
    else:
        l += i
print(l)
print(c)
