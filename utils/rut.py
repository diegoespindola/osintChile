from utils import strings

if __name__ == "__main__":
    print('Esto no se ejecuta solo, es para ser llamado desde el programa principal')


def formatRut(rut):
    cuerpo = strings.right('000' + rut.split('-')[0], 9)
    dv = rut.split('-')[1]

    return str(int(strings.left(strings.right(cuerpo,9),3))) + '.' + strings.left(strings.right(cuerpo,6),3) + '.' + strings.right(cuerpo,3) + '-' + dv

