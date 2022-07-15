from datetime import date
import json
import requests
import codecs
if __name__ == "__main__":
    print('Esto no se ejecuta solo, es para ser llamado desde el programa principal')


def busqueda(patente):
    busquedaSoapOK(patente)


def busquedaSoapOK(patente):

    
    urlSOAPRoted = 'uggcf://jjj.fbncbx.py/frthebf-bayvar/FBNC/ohfpn_gvcb_iru.cuc'
    urlSOAP = codecs.decode(urlSOAPRoted, 'rot_13')  
    print('--==<Datos desde SOAP OK>==--')
    paramSOAP = {'patente':patente, 'dinamico':'true'}
 
    page  = requests.post(url=urlSOAP, data=paramSOAP)
    if page.status_code==200:
        datosJson = json.loads(page.text)
        if datosJson['res']=='OK':
            print('     Patente             :', datosJson['patente'])
            print('     DV                  :', datosJson['dv'])
            print('     TipoVehiculo        :', datosJson['tipo_veh'])

            print(' ')
        else:
            print('  Error en respuesta:', page.content)
    else:
        print("        Error en request:", page.status_code)


    
    
    
