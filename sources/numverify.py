import argparse
import requests
import json
import codecs
from bs4 import BeautifulSoup
import hashlib

def busqueda(telefono):
    busquedaNumVerify(telefono)

def busquedaNumVerify(telefono):

    urlNumVrfyHomeRoted = 'uggc://ahzirevsl.pbz/'
    urlNumVrfyHome = codecs.decode(urlNumVrfyHomeRoted, 'rot_13')

    pageKey = requests.get(url=urlNumVrfyHome)
    if pageKey.status_code == 200:
        soup = BeautifulSoup(pageKey.content, 'html.parser')
        secret_key = soup.find_all('input',type='hidden')[1]['value']

        concat=telefono + secret_key
        api_key = hashlib.md5( concat.encode('utf-8')).hexdigest()

        urlNumverifyRoted = 'uggcf://ahzirevsl.pbz/cuc_urycre_fpevcgf/cubar_ncv.cuc?frperg_xrl='

        urlNumverify = codecs.decode(urlNumverifyRoted, 'rot_13') + api_key + '&number=' + telefono
        print(' ')
        print('  --==< Datos desde NumVerify.com>==--')

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
    else:
        print("  Error en request:", pageKey.status_code)                        

if __name__ == "__main__":
    print('Esto no se ejecuta solo, es para ser llamado desde el programa principal')
