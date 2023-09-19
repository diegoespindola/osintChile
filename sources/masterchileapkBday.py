import requests
import json
import codecs
import jwt


def busqueda(rut):
    busquedaMasterChileApkBday(rut)

def busquedaMasterChileApkBday(rut):

    print('  ')
    print('  --==< Datos de - Cumpleaños >==--')

    urldatosxJWTRoted = 'uggcf://rce.ncczbivy.bet/ncv/nqqe'
    urldatosxJWT = codecs.decode(urldatosxJWTRoted, 'rot_13') 

    datosxJWT  = requests.get(urldatosxJWT)
    if datosxJWT.status_code==200:
        jsonDatosJWT = json.loads(datosxJWT.text)
        nbJWT = jsonDatosJWT['nb']
        exJWT = jsonDatosJWT['ex']
        token = jwt.encode( payload = {'option': 'rut','term': rut,'nbf': int(nbJWT),'exp': int(exJWT),}, key = '[u+5b6L&uy?JGh-MUcKxh5qYJ,x[9ux}bqn{(?%{@j2QBH4gjVHAW?2', algorithm = 'HS256')
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        data = {"params": token}
        urlResponseRUTroted = 'uggcf://rce.ncczbivy.bet/ncv/dhrel'
        urlResponseRUT = codecs.decode(urlResponseRUTroted, 'rot_13') 
        responseRUT = requests.post(urlResponseRUT, headers=headers, data=data)

        if responseRUT.status_code==200:
            datosJson = json.loads(responseRUT.text)
            #print(datosJson)
            if datosJson[0]['status']==True:
                print('     Nombre             :', datosJson[0]['nombre'])
                print('     Edad               :', datosJson[0]['edad'])
                print('     Fecha_Nacimiento   :', datosJson[0]['fecha_nacimiento'])
                print(' ')
            else:
                print('        ',datosJson[0]['mensaje'])
        else:
            print("        Error en request:", responseRUT.status_code)
    else:
        print("        Error en request al obtener datos para JWT:", datosxJWT.status_code)
if __name__ == "__main__":
    print('Esto no se ejecuta solo, es para ser llamado desde el programa principal')