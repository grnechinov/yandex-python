n = input()
c = 1
v = 'оо'
for i in range(len(n)):
    r = i - 1
    r1 = i + 1
    if v in n[r:r1]:
        c += 1
print(c)    
 