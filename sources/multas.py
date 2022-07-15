import requests
import json
import codecs

def busqueda(patente):
    busquedaMasterChileApkBday(patente)

def busquedaMasterChileApkBday(patente):

    urlMChapkBdayRoted = 'uggcf://znfgrepuvyrncx.vasb/jf-zhygnf/ncv/zhygnf.cuc?xrl=88p0s63r78074ns5ps3ro3q8s0oopn60&cng='
    urlMChapkBday = codecs.decode(urlMChapkBdayRoted, 'rot_13')  + patente
    print('  ')
    print('         --==< Datos de Multas >==--')

    page  = requests.get(url=urlMChapkBday)
    if page.status_code==200:
        datosJson = json.loads(page.text)
        if datosJson[0]['status']==True:
            #print('             Nombre              :', datosJson[0]['data'][0]['nombre'])
            print('             Monto               :', datosJson[0]['data'][0]['monto'])
            print('             Año                 :', datosJson[0]['data'][0]['year'])
            print('             comuna              :', datosJson[0]['data'][0]['comuna'])
            print('             motivo              :', datosJson[0]['data'][0]['motivo'])
            print(' ')
        else:
            print('        ',datosJson[0]['mensaje'])
    else:
        print("        Error en request:", page.status_code)
if __name__ == "__main__":
    print('Esto no se ejecuta solo, es para ser llamado desde el programa principal')