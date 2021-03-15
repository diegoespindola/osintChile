import argparse
import re
import requests
import urllib.parse
import json
import base64
from bs4 import BeautifulSoup
import codecs

def busqueda(rut):
    busquedaRutSii(rut)

def busquedaRutSii(rut):

    
    #Fuente: https[://]zeus[.]sii[.]cl[/]cvc[/]stc[/]stc[.]html
    print('  --==<Datos desde Sii>==--')
    print('  Si tiene inicio de actividades deberia estar acá')
    #vamos por el captcha
    urlSiiGetCaptcha = 'uggcf://mrhf.fvv.py/pip_ptv/fgp/PIvrjPncgpun.ptv'
    paramCaptcha = urllib.parse.urlencode({'oper':0})
    paramCaptcha = paramCaptcha.encode('ascii')

    htmlGetCaptcha = requests.post(url=codecs.decode(urlSiiGetCaptcha, 'rot_13'),data=paramCaptcha).text
    captchaJson = json.loads(htmlGetCaptcha)
    captchaB64 = captchaJson.get('txtCaptcha')
    txtCaptchaDecoded = base64.b64decode(captchaB64.encode('ascii')).decode('ascii')

    paramDatos = urllib.parse.urlencode({
          'RUT' : rut.split('-')[0],
          'DV' : str(rut.split('-')[1]).upper,
          'PRG' : 'STC',
          'OPC' : 'NOR',
          'txt_code' : txtCaptchaDecoded[36:40] ,
          'txt_captcha' : captchaB64 })

    paramDatos = paramDatos.encode('ascii')
    urlSiiDatos = 'uggcf://mrhf.fvv.py/pip_ptv/fgp/trgfgp'
    
    page = requests.post(url=codecs.decode(urlSiiDatos, 'rot_13'), data=paramDatos)
    
    soup = BeautifulSoup(page.text, 'html.parser')
    divs = soup.find_all('div')
 
    regexp = re.compile("Contribuyente presenta Inicio de Actividades: (.*?)<", re.MULTILINE)
    match = regexp.search(page.text)
    if match:
        contribuyente = match.group(1)
    else:
        contribuyente = ""
    
    if(contribuyente=='SI'):
        print('     Rut                      :', divs[7].get_text())
        print('     Razon Social             :', divs[5].get_text())

        trList = soup.find('table').find_all('tr')
        for actividad in trList[1:]:
            tdList = actividad.find_all('td')

            print('        Giro                     :', tdList[0].find('font').get_text())
            print('        Codigo                   :', tdList[1].find('font').get_text())
            print('        Categoria                :', tdList[2].get_text())
            print('        Afecta                   :', tdList[3].get_text())
            print('        Fecha                    :', tdList[4].get_text())
            print(' ')
    
    else:
            print('\n   --Contribuyente no presenta inicio de Actividades-- \n')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='OSINTchile', description='Busqueda automatica de fuentes abiertas de chile')
    parser.add_argument('-rut', type=str, nargs='?', help='Rut de la persona a buscar, con formato: 11111111-1 ')
    parametros = parser.parse_args()

    if not (parametros.rut) :
        parser.print_help()
    else:
        busquedaRutSii(parametros.rut)
