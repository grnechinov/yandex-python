memory = list()


def do_bet(number, money):
    if number not in memory and 10 >= number > 0 != money:
        memory.append(number)
        print(f'Ваша ставка в размере {money} на лошадь {number} принята')
    else:
        print('Что-то пошло не так, попробуйте еще раз')
