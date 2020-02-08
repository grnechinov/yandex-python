c = 0
a = 1
while a > 0:
    a = float(input())
    if a > 1000:
        c = c + a * 0.95
    elif a < 0:
        break
    else:
        c += a
print(c)