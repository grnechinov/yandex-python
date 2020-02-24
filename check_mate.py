n = int(input())
b = []
stroka = "ABCDEFGHI"
if n < 10:
    b = [[j+1 for j in range(9)] for sch in range(9)]
for sch in range(n - 1, -1, -1):
    for j in range(n):
        print(stroka[j] + str(b[j][sch]), end=' ')
    print()