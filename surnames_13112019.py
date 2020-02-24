men_works = set()
men = int(input())
cout = 0
for sch in range(men):
    name = input()
    if name in men_works:
        cout += 1
    else:
        men_works.add(name)
print(cout)