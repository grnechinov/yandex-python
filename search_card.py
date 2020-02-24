global base


def hello(name):
    print("Здравствуйте, ", name, "!", " Вашу карту ищут...", sep="")


def search_card(name):
    if name in base:
        card_number = base.index(name) + 1
        print(f"Ваша карта с номером {card_number} найдена")
    else:
        print("Ваша карта не найдена")
