import myClasses.Classes as clases
import requests
import json
import codecs

def busqueda(objetivo):
    return(busquedaPacienteUC(objetivo))

def busquedaPacienteUC(objetivo):
    
    urlSaludUCRoted = 'uggcf://ncvtj.hppuevfghf.py/ntraqnnzohyngbevn-cebq/Cnpvragrf?gvcbVqCnpvragr=EHA&cnvfVqragvsvpnqbe=PY&vqCnpvragr='
    urlSaludUC = codecs.decode(urlSaludUCRoted, 'rot_13')  + objetivo.Rut
    
    page  = requests.get(url=urlSaludUC)
    statusCode, statusReason = page.status_code, page.reason
    
    if page.status_code==200:
        datosJson = json.loads(page.text)
        if datosJson['statusCod'] == 'OK':
            datosPersona = clases.DatosPersonales(Source='Salud 1')
            datosPersona.PrimerNombre = datosJson['listaPacientes'][0]['primerNombre']
            datosPersona.SegundoNombre = datosJson['listaPacientes'][0]['segundoNombre']
            datosPersona.ApellidoPaterno = datosJson['listaPacientes'][0]['primerApellido']
            datosPersona.ApellidoMaterno = datosJson['listaPacientes'][0]['segundoApellido']
            datosPersona.NombreCompleto = datosJson['listaPacientes'][0]['nombreCompleto']
            datosPersona.RutFormateado = datosJson['listaPacientes'][0]['numeroDocumentoFormateado']

            telefono = datosJson['listaPacientes'][0]['numeroTelefonoPrincipal']
            if (len(telefono)>0):
                objetivo.Telefonos.append(clases.Telefono(number = telefono, Source='Salud 1'))

            correo = datosJson['listaPacientes'][0]['email']
            if (len(correo)>0):
                objetivo.Correos.append(clases.Email(address = correo, Source='Salud 1'))

            objetivo.DatosPersonales.append(datosPersona)        
        else:
            statusCode = -1
            statusReason = datosJson['statusDesc']
    return(objetivo, statusCode, statusReason)
    
if __name__ == "__main__":
    print('Esto no se ejecuta solo, es para ser llamado desde el programa principal')
