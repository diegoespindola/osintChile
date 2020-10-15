import argparse
import requests
import json
import codecs

def busqueda(rut):
    busquedaPacienteUC(rut)

def busquedaPacienteUC(rut):

    urlSaludUCRoted = 'uggcf://ncvtj.hppuevfghf.py/ntraqnnzohyngbevn-cebq/Cnpvragrf?gvcbVqCnpvragr=EHA&cnvfVqragvsvpnqbe=PY&vqCnpvragr='
    urlSaludUC = codecs.decode(urlSaludUCRoted, 'rot_13')  + rut
    print('  ')
    print('  --==< Datos desde Centro medico 1 >==--')
    print('  Si se atendio en este centro, podremos saber su nombre')

    page  = requests.get(url=urlSaludUC)
    if page.status_code==200:
        datosJson = json.loads(page.text)
        if datosJson['statusCod'] == 'OK':
            print('     Primer nombre               :', datosJson['listaPacientes'][0]['primerNombre'])
            print('     Segundo nombre              :', datosJson['listaPacientes'][0]['segundoNombre'])
            print('     Primer apellido             :', datosJson['listaPacientes'][0]['primerApellido'])
            print('     Segundo apellido            :', datosJson['listaPacientes'][0]['segundoApellido'])
            print('     Nombre completo             :', datosJson['listaPacientes'][0]['nombreCompleto'])
            print('     Numero documento formateado :', datosJson['listaPacientes'][0]['numeroDocumentoFormateado'])
            print('     Numero telefono aproximado  :', datosJson['listaPacientes'][0]['numeroTelefonoPrincipal'])
            print('     email aproximado            :', datosJson['listaPacientes'][0]['email'])
            print(' ')
        else:
            print(datosJson['statusDesc'])
    else:
        print("  Error en request:", page.status_code)
if __name__ == "__main__":
    print('Esto no se ejecuta solo, es para ser llamado desde el programa principal')
