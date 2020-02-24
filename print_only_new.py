memory = list()


def print_only_new(message):
    if message not in memory:
        memory.append(message)
        print(message)
