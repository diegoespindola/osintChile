import argparse
import requests
import json
import codecs

def busqueda(rut):
    busquedaMasterChileApkBday(rut)

def busquedaMasterChileApkBday(rut):

    urlMChapkBdayRoted = 'uggcf://znfgrepuvyrncx.vasb/jf-oveguqnli3/ncv/?ehg='
    urlMChapkBday = codecs.decode(urlMChapkBdayRoted, 'rot_13')  + rut
    print('  ')
    print('  --==< Datos de - Cumpleaños >==--')

    page  = requests.get(url=urlMChapkBday)
    if page.status_code==200:
        datosJson = json.loads(page.text)
        if datosJson[0]['status']==True:
            print('     Nombre             :', datosJson[0]['nombre'])
            print('     Edad               :', datosJson[0]['edad'])
            print('     Fecha_Nacimiento   :', datosJson[0]['fecha_nacimiento'])

            print(' ')
        else:
            print('        ',datosJson[0]['mensaje'])
    else:
        print("        Error en request:", page.status_code)
if __name__ == "__main__":
    print('Esto no se ejecuta solo, es para ser llamado desde el programa principal')