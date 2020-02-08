def take_large_banknotes(banknotes):
    v = []
    for i in banknotes:
        if int(i) > 10:
            v.append(i)
    return v

