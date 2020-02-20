import string
import random


def generate_password(m):
    list_of_string = list(set(string.ascii_letters +
                              string.digits).difference({'I', 'l', '1', 'o', 'O', '0'}))
    list_of_string.sort()
    sp = random.sample(list_of_string, m)
    _string = ''.join(sp)
    return _string


def main(n, m):
    list_of_password = []
    for i in range(n):
        password = generate_password(m)
        while password in list_of_password:
            password = generate_password(m)
        list_of_password.append(password)
    return list_of_password

print("Случайный пароль из 7 символов:", generate_password(7))
print("10 случайных паролей длиной 15 символов:")
print(*main(10, 15), sep="\n")