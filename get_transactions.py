transactions = {}


def get_transactions(data):
    pref = "kol-"

    if data == 'print_it':

        for transaction in transactions.items():
            operation = transaction[0]
            amount = transaction[1]

            if not operation.startswith(pref):
                print(f"{transactions[pref + operation]} {operation} {amount}")

        return

    tmp_list_1 = data.split(':')
    tmp_list_2 = tmp_list_1[0].split('-')
    # phone = tmp_list_2[0]
    operation = tmp_list_2[1]
    amount = int(tmp_list_1[1])

    transactions[operation] = transactions.get(operation, 0) + amount
    transactions[pref + operation] = transactions.get(pref + operation, 0) + 1

