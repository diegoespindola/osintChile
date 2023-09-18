import json
import requests
import time
from utils import rut as rutUtils
from bs4 import BeautifulSoup
import codecs
import datetime

def get_age_from_rut(rut):
    today_date = datetime.datetime.now()
    slope = 3.3363697569700348e-06
    intercept = 1932.2573852507373
    birth_date = rut * slope + intercept
    birth_date_year = int(birth_date)
    birth_date_month = round((birth_date - birth_date_year) * 12)
    birth_date = datetime.datetime(birth_date_year, birth_date_month, 1)
    age = today_date - birth_date
    age_in_years = int(age.days / 365.25)
    return [age_in_years, birth_date_month, birth_date_year]

def get_chatbot_response(user_message):
    url = "https://chatbot-ji1z.onrender.com/chatbot-ji1z"
    
    data = {
        "messages": [
            {
                "role": "user",
                "content": user_message
            }
        ]
    }

    headers = {
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(url, data=json.dumps(data), headers=headers, timeout=(10, 20))
        response_code = response.status_code

        if response_code == 200:
            response_json = response.json()
            content = response_json["choices"][0]["message"]["content"]
            return content
        else:
            return f"Error al enviar la solicitud. Código de estado: {response_code}"
    except requests.exceptions.RequestException as e:
        return f"Error en la comunicación con el ChatGPT: {str(e)}"
    except json.JSONDecodeError as e:
        return f"Error al manejar la respuesta del ChatGPT: {str(e)}"
    finally:
        # Agregar un tiempo de espera entre solicitudes para evitar sobrecargar el servidor
        time.sleep(0.8)

def busqueda(rut):
    busquedaNombrerutyFirma(rut)

def busquedaNombrerutyFirma(rut):
    params = {'term': rutUtils.formatRut(rut)}
    headers = {
        'Alt-Used': 'www.nombrerutyfirma.com',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Referer': 'https://www.nombrerutyfirma.com/'
    }
    urlNryfRoted = 'uggcf://jjj.abzoerehglsvezn.pbz/ehg'
    urlNryf = codecs.decode(urlNryfRoted, 'rot_13')

    page = requests.post(url=urlNryf, params=params, headers=headers)
    print('  --==<Datos desde NombreRutyFirma>==--')
    print('  Si está inscrito en SERVEL debería aparecer aquí')
    if page.status_code == 200:
        soup = BeautifulSoup(page.content, 'html.parser')
        tabla = soup.find('tr', tabindex='1')
        if tabla:
            datosTD = tabla.find_all('td')

            raw_rut = datosTD[1].get_text().replace('.', '').split('-')[0]
            rut = float(raw_rut)

            months = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre']

            result = get_age_from_rut(rut)
            print('     Nombre                   :', datosTD[0].get_text())
            print('     RUT                      :', datosTD[1].get_text())
            print(f'     Edad aproximada          : {result[0]}')
            print('     Sexo                     :', datosTD[2].get_text())
            print('     Direccion                :', datosTD[3].get_text())
            print('     Ciudad/Comuna            :', datosTD[4].get_text())
            print(" ")
            print("Consultando a ChatGPT donde queda la comuna donde vive la persona...")

            response = get_chatbot_response("Dime en qué parte de Chile queda " + datosTD[4].get_text() + " y dame sus coordenadas. Tu respuesta debe ser de menos de 500 caracteres")

            print(" ")
            print("La respuesta de ChatGPT es la siguiente:", response)
            print(" ")

        else:
            print('  No hay datos')
    else:
        print("  Error en request:", page.status_code)      

if __name__ == "__main__":
    print('Esto no se ejecuta solo, es para ser llamado desde el programa principal')
