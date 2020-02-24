sch = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц',
     'ч', 'ш', 'щ', 'ъ', 'ы', 'ь',
     'э', 'ю', 'я']
b = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О',
     'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э',
     'Ю', 'Я']


def encrypt_caesar(msg, shift):
    r = ""
    for x in msg:
        if x in sch:
            ind = sch.index(x) % len(sch)
            r += sch[(ind + shift) % len(sch)]
        elif x in b:
            ind = b.index(x) % len(sch)
            r += b[(ind + shift) % len(sch)]
        else:
            r += x
    return r


def decrypt_caesar(msg, shift):
    r = ""
    for x in msg:
        if x in sch:
            ind = sch.index(x)
            r += sch[ind - shift]
        elif x in b:
            ind = b.index(x)
            r += b[ind - shift]
        else:
            r += x
    return r
