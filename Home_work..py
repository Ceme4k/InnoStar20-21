a = float(input())
b = float(input())
c = input()
if c == "*":
    print(a * b)
elif c == "/":
    if b != 0:
        print(a / b)
    else:
        print(888888)
elif b == 0 or a == 0:
    print(0)
elif c == "-":
    print(a - b)
elif c == "+":
    print(a + b)
else:
    print("888888")
