memory = list()


def parrot(phrase):
    if phrase in memory:
        print(phrase)

    memory.append(phrase)

