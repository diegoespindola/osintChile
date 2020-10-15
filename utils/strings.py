if __name__ == "__main__":
    print('Esto no se ejecuta solo, es para ser llamado desde el programa principal')

def left(s, amount):
    return s[:amount]


def right(s, amount):
    return s[-amount:]


def mid(s, offset, amount):
    return s[offset:offset+amount]