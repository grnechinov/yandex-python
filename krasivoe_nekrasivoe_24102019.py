a = int(input())
if ((a // 100) + (a % 10)) / 2 == ((a // 10) % 10):
    print("ОК")
elif ((a // 100) + (a // 10) % 10) / 2 == (a % 10):
    print("ОК")
elif ((a % 10) + ((a // 10) % 10)) / 2 == (a // 100):
    print("ОК")
else:
    print("Жаль, вы ввели обычное число")