n = int(input()) 
for i in range(n):
    a = input()
    if a[:3] == 'не ' or a[:3] == 'Не ':
        print(a[3:])
    else:
        print(a)