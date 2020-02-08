n = int(input()) 
for i in range(n):
    a = input()
    if a[:2] == '%%':
        print(a[2:])
    elif a[:4] != '####':
        print(a)