import requests
from utils import rut as rutUtils
from bs4 import BeautifulSoup
import codecs
import sources.multas as multas

def busqueda(rut=None, patente=None):
    busquedaVolanteomaleta(rut=rut, patente=patente)

def busquedaVolanteomaleta(rut=None, patente=None):
    if (rut):
        params = {'term': rutUtils.formatRut(rut)}
        urlVoMRoted = 'uggcf://jjj.ibynagrbznyrgn.pbz/ehg'
        urlVoM = codecs.decode(urlVoMRoted, 'rot_13')

        
        page = requests.post(urlVoM, params=params)
        print('  --==<Datos desde VolanteoMaleta>==--')
        if page.status_code == 200:
            soup = BeautifulSoup(page.content, 'html.parser')
            tbody = soup.find('tbody')
            datosTR = tbody.find_all('tr')
            if len(datosTR)>0:
                for tr in datosTR:
                    if tr:
                        datosTD = tr.find_all('td')
                        print('     RUT                       :', datosTD[4].get_text())
                        print('     Patente                   :', datosTD[0].get_text())
                        print('     Tipo                      :', datosTD[1].get_text())
                        print('     Marca                     :', datosTD[2].get_text())
                        print('     Modelo                    :', datosTD[3].get_text())
                        print('     Nro. Motor                :', datosTD[5].get_text())
                        print('     Año                       :', datosTD[6].get_text())
                        ''' print('     Nombre a Rutificador      :', datosTD[7].get_text())   '''
                        print(" ")

                        multas.busqueda(patente = datosTD[0].get_text())

                    else:
                        print('  No hay datos')
            else:
                print('  No hay datos')
        else:
            print("  Error en request:", page.status_code)  

    elif(patente):
        params = {'term': patente}
        urlVoMRoted = 'uggcf://jjj.ibynagrbznyrgn.pbz/cng'
        urlVoM = codecs.decode(urlVoMRoted, 'rot_13')

        
        page = requests.post(urlVoM, params=params)
        print('  --==<Datos desde VolanteoMaleta>==--')
        if page.status_code == 200:
            soup = BeautifulSoup(page.content, 'html.parser')
            tbody = soup.find('tbody')
            datosTR = tbody.find_all('tr')
            if len(datosTR)>0:
                for tr in datosTR:
                    if tr:
                        datosTD = tr.find_all('td')
                        print('     RUT                       :', datosTD[4].get_text())
                        print('     Patente                   :', datosTD[0].get_text())
                        print('     Tipo                      :', datosTD[1].get_text())
                        print('     Marca                     :', datosTD[2].get_text())
                        print('     Modelo                    :', datosTD[3].get_text())
                        print('     Nro. Motor                :', datosTD[5].get_text())
                        print('     Año                       :', datosTD[6].get_text())
                        ''' print('     Nombre a Rutificador      :', datosTD[7].get_text())   '''
                        print(" ")

                        multas.busqueda(patente = datosTD[0].get_text())

                    else:
                        print('  No hay datos')
            else:
                print('  No hay datos')
        else:
            print("  Error en request:", page.status_code)  
                
        
if __name__ == "__main__":
    print('Esto no se ejecuta solo, es para ser llamado desde el programa principal')