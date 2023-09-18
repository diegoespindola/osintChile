from bs4 import BeautifulSoup
import requests

def api2_conversor(nombre):
    respuesta = requests.get('https://ws.rutificador.app/call-rutificador-v2/?opcion=nombre&nombre=%s' % nombre)
    html_data = respuesta.text
    s = BeautifulSoup(html_data, 'html.parser').table
    h, [_, *d] = [i.text for i in s.tr.find_all('th')], [[i.text for i in b.find_all('td')] for b in s.find_all('tr')]
    json = [dict(zip(h, i)) for i in d]
    return json

def api1_conversor(nombre):
    URL = 'https://www.nombrerutyfirma.com/buscar'
    params = {'term': nombre}
    peticion = requests.post(URL, data=params)
    if peticion.status_code == 200:
        html_code = peticion.text
    s = BeautifulSoup(html_code, 'html.parser').table
    h, [_, *d] = [i.text for i in s.tr.find_all('th')], [[i.text for i in b.find_all('td')] for b in s.find_all('tr')]
    json = [dict(zip(h, i)) for i in d]
    return json

def normalizar(s):
    remplazos = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )
    for a, b in remplazos:
        s = s.replace(a, b)
    s = s.upper()
    return s

# Define la variable maxResult
maxResult = 150

def buscar_info_por_nombre(nombre):
    x = 0
    comuna = False

    print('---------------- Rutificador (RMax:%d) ------------------' % maxResult)
    print('(Usar 2 nombres o 2 apellidos para mejores resultados)')
    print(' ')

    # Establecer el nombre desde el argumento de la función
    nombre = input('Ingrese el nombre: ')
    print(' ')

    while x == 0:
        validador = normalizar(input('¿Desea filtrar por comuna? (S/N): '))

        if validador == 'S':
            x = 1
            comuna = True
        elif validador == 'N':
            break
        else:
            continue

    if not comuna:
        print(' ')
        print('Cargando...')
        print(' ')

        try:
            datos = api1_conversor(nombre)

            for i in range(0, len(datos)):
                # Imprimir información
                print('Nombre: %s' % datos[i]['Nombre'])
                print('RUT: %s' % datos[i]['RUT'])
                print('Género: %s' % datos[i]['Sexo'])
                print('Dirección: %s' % normalizar(datos[i]['Dirección']))
                print('Comuna/Ciudad: %s' % normalizar(datos[i]['Ciudad/Comuna']))
                print('----------------------------------')
                print('----------------------------------')

            # Imprimir cantidad de resultados
            print(' ')
            print('Resultados: %d/%d (API 1)' % (len(datos), maxResult))
            print(' ')

        except:
            datos = api2_conversor(nombre)

            for i in range(0, len(datos)):
                # Imprimir información
                print('Nombre: %s' % datos[i]['Nombre'])
                print('RUT: %s' % datos[i]['RUT'])
                print('Género: %s' % datos[i]['Género'])
                print('Dirección: %s' % normalizar(datos[i]['Dirección']))
                print('Comuna/Ciudad: %s' % normalizar(datos[i]['Comuna']))
                print('----------------------------------')
                print('----------------------------------')

            # Imprimir cantidad de resultados
            print(' ')
            print('Resultados: %d/%d (API 2)' % (len(datos), maxResult))
            print(' ')

    else:
        print(' ')
        x = 0

        comuna = normalizar(input('Ingrese la comuna: '))
        print(' ')
        print('Cargando...')
        print(' ')

        try:
            datos = api1_conversor(nombre)
            cantidad = 0

            for i in range(0, len(datos)):

                if normalizar(datos[i]['Ciudad/Comuna']).find(comuna) > -1:
                    cantidad += 1
                    # Imprimir información
                    print('Nombre: %s' % datos[i]['Nombre'])
                    print('RUT: %s' % datos[i]['RUT'])
                    print('Género: %s' % datos[i]['Sexo'])
                    print('Dirección: %s' % normalizar(datos[i]['Dirección']))
                    print('Comuna/Ciudad: %s' % normalizar(datos[i]['Ciudad/Comuna']))
                    print('----------------------------------')
                    print('----------------------------------')

            # Imprimir cantidad de resultados
            print(' ')
            print('Resultados: %d/%d (API 1)' % (cantidad, maxResult))
            print(' ')

        except:
            datos = api2_conversor(nombre)
            cantidad = 0

            for i in range(0, len(datos)):

                if normalizar(datos[i]['Ciudad/Comuna']).find(comuna) > -1:
                    cantidad += 1
                    # Imprimir información
                    print('Nombre: %s' % datos[i]['Nombre'])
                    print('RUT: %s' % datos[i]['RUT'])
                    print('Género: %s' % datos[i]['Género'])
                    print('Dirección: %s' % normalizar(datos[i]['Dirección']))
                    print('Comuna/Ciudad: %s' % normalizar(datos[i]['Comuna']))
                    print('----------------------------------')
                    print('----------------------------------')

            # Imprimir cantidad de resultados
            print(' ')
            print('Resultados: %d/%d (API 2)' % (cantidad, maxResult))
            print(' ')

if __name__ == "__main__":
    print('Esto no se ejecuta solo, es para ser llamado desde el programa principal')
