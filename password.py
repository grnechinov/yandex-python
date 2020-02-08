n = input()
b = input()
if len(n) < 8:
    print('Короткий!')
elif '123' in n:
    print('Простой!')
elif b != n:
    print('Различаются.')
else:
    print('OK')