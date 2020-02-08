a = int(input())
c = (a // 100) + ((a // 10) % 10)
s = ((a // 10) % 10) + (a % 10)
print(c, s, sep='')
