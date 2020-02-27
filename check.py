total = 0
pr = []


def add_item(item_name, item_cost):
    global total
    global pr
    total += item_cost
    stroke = str(item_name) + ' - ' + str(item_cost)
    pr.append(stroke)


def print_receipt():
    global sch
    global total
    global pr
    sch = 0
    if len(pr) != 0:
        sch += 1
        print('Чек ', sch, '. Всего предметов: ', len(pr), sep='')
        for k in pr:
            print(k)
        print('Итого:', total)
        print('-----')
        pr.clear()
        total = 0

add_item('Блокнот', 100)
print_receipt()

add_item('Ручка', 70)
print_receipt()
print_receipt()

add_item('Булочка', 15)
add_item('Булочка', 15)
add_item('Чай', 5)
print_receipt()

add_item('Булочка', 15)
add_item('Булочка', 15)
# (Отменить чек) - этот чек не печатаем