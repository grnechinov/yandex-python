n = int(input())
a = []
c = []
for i in range(n):
    a.append(input())
v = int(input())
for j in range(v):
    c.append(input())
for u in range(len(c)):
    if a in c:
        print(a)