daily_food = [0, 150, 150]


def count_food(number_of_date):

    amount = 0

    for i in number_of_date:
        amount += daily_food[i - 1]

    return amount

