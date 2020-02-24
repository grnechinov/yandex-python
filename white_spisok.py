n = int(input())
a = []
c = []
for sch in range(n):
    a.append(input())
sch = int(input())
for j in range(sch):
    c.append(input())
for u in range(len(c)):
    if a in c:
        print(a)