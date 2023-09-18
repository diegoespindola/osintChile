import requests
import json

def busqueda(rut):
    busquedaPacienteIndisa(rut)

def busquedaPacienteIndisa(rut):
    # Definir la URL a la que deseas enviar la solicitud POST
    url = 'https://agenda.eniax.cl/api/v1/enroll_patient/consulta_indisa/' + rut

    # Datos que deseas enviar en el cuerpo de la solicitud POST (en este ejemplo, un diccionario)
    data = {
        'medical_insurance': '53',
        'cod_paciente': rut  # Aquí usamos el rut que se pasa como argumento
    }

    # Realizar la solicitud POST
    response = requests.post(url, data=data)

    print('  ')
    print('  --==< Datos de la clinica indisa >==--')
    print('Aqui podremos saber si la persona se atendio alguna vez')

    if response.status_code == 200:
        # Obtener la respuesta del servidor en formato JSON
        datosJson = response.json()

        # Extraer el valor de "status" de la respuesta JSON
        status = datosJson.get('status')
        
        if status == 'registered_patient':
            print('La persona se ha atendido aqui')
            print('  ')
        elif status == 'unregistered_patient':
            print('La persona nunca se ha atendido aqui')
            print('  ')
        else:
            print('Estado desconocido:', status)
    else:
        print('La solicitud POST falló. Código de estado HTTP:', response.status_code)

if __name__ == "__main__":
    print('Esto no se ejecuta solo, es para ser llamado desde el programa principal')
