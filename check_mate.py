n = int(input())
b = []
stroka = "ABCDEFGHI"
if n < 10:
    b = [[j+1 for j in range(9)] for i in range(9)]
for i in range(n-1, -1, -1):
    for j in range(n):
        print(stroka[j] + str(b[j][i]), end=' ')
    print()