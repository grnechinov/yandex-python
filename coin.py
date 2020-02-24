n = input()
c = 1
sch = 'оо'
for sch in range(len(n)):
    r = sch - 1
    r1 = sch + 1
    if sch in n[r:r1]:
        c += 1
print(c)    
 