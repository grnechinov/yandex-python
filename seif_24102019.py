name = int(input())
name1 = (name % 10)
name10 = (((name % 100) - name1) / 10)
name100 = (name // 100)
if name1 == name10 == name100:
    print('В числе все цифры одинаковые')
elif name1 == name10 > name100 or\
     name1 == name10 < name100 or\
     name1 == name100 > name10 or\
     name1 == name100 < name10 or\
     name10 == name100 > name1 or\
     name10 == name100 < name1:
    print('В числе две цифры одинаковые')
else:
    print('ОК')
