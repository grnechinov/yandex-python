v = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц',
     'ч', 'ш', 'щ', 'ъ', 'ы', 'ь',
     'э', 'ю', 'я']
b = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О',
     'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э',
     'Ю', 'Я']


def encrypt_caesar(msg, shift):
    r = ""
    for x in msg:
        if x in v:
            ind = v.index(x) % len(v)
            r += v[(ind + shift) % len(v)]
        elif x in b:
            ind = b.index(x) % len(v)
            r += b[(ind + shift) % len(v)]
        else:
            r += x
    return r


def decrypt_caesar(msg, shift):
    r = ""
    for x in msg:
        if x in v:
            ind = v.index(x)
            r += v[ind - shift]
        elif x in b:
            ind = b.index(x)
            r += b[ind - shift]
        else:
            r += x
    return r
