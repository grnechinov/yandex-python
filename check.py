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
    if len(pr) != 0:
        sch += 1
        print('Чек', sch, '.Всего предметов: ', len(pr), sep='')
        for k in pr:
            print(k)
        print('Итого:', total)
        print('-----')
        pr.clear()
        total = 0
