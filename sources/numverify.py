import argparse
import requests
import json
import codecs

def busqueda(telefono):
    busquedaNumVerify(telefono)

def busquedaNumVerify(telefono):
    urlNumverifyRoted = 'uggc://ncvynlre.arg/ncv/inyvqngr?sbezng=1&npprff_xrl=3888s896p1779qsn549o4o9r1pp71995&ahzore='

    urlNumverify = codecs.decode(urlNumverifyRoted, 'rot_13')  + telefono
    print(' ')
    print('  --==< Datos desde NumVerify.com >==--')

    page = requests.get(url=urlNumverify)
    if page.status_code==200:
        if ( page.text != 'Unauthorized'):
            datosJson = json.loads(page.text)
            if 'success' in datosJson and datosJson['success']== False :
                    print('  ' + datosJson['error']['info'])
            else:
                if 'valid' in  datosJson and datosJson['valid'] == True:
                    print('     Numero                  :', datosJson['number'])
                    print('     Formato internacional   :', datosJson['international_format'])
                    print('     Codigo de Pais          :', datosJson['country_code'])
                    print('     Pais                    :', datosJson['country_name'])
                    print('     Carrier                 :', datosJson['carrier'])
                    print('     Tipo de linea           :', datosJson['line_type'])
                    print(' ')
                else:
                    print('  Telefono invalido')
        else:
            print(datosJson['  No autorizado'])
    else:
        print("  Error en request:", page.status_code)            

if __name__ == "__main__":
    print('Esto no se ejecuta solo, es para ser llamado desde el programa principal')