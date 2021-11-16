a = int(input())
b = list(map(int, input().split()))
c = 0
for i in range(len(b)):
    c += b[i]
print(c)
