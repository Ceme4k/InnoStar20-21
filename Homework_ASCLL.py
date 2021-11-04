a = input()
if 64 < ord(a) < 91 or 96 < ord(a) < 123:
    if ord(a) < 91:
        print(chr(ord(a) + 32))
    else:
        print(chr(ord(a) - 32))
else:
    print("Ошибка")
