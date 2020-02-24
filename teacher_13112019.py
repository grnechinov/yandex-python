n = int(input())
lst = [set(input() for _ in range(int(input()))) for _ in range(n)]
res = lst[0]
for sch in lst:
    res = res.intersection(sch)
print(*sorted(res), sep='\n')
