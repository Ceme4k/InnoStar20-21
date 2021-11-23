n = int(input())
students = list(map(int, input().split()))
petya = int(input())
k = 1
for student in students:
    if student >= petya:
        k += 1
print(k)
