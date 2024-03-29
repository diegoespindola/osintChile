import argparse
import requests
import json
from PIL import Image
import codecs
import os

def busqueda(telefono):
    print(' ')
    print('  --==< Datos desde Celuzador >==--')
    ruta = busquedaCeluzador(telefono)
    if ruta :
        print(f'     Foto de perfil para el número {telefono} guardada en "{ruta}"')

def busquedaCeluzador(telefono):
    urlceluzadorRoted = 'uggcf://pryhmnqbe.bayvar/pryhmnqbeNcv.cuc'
    urlceluzador = codecs.decode(urlceluzadorRoted, 'rot_13')

    headers = {
        'User-Agent': 'CeludeitorAPI-TuCulitoSacaLlamaAUFAUF '
    }
    response = requests.post(urlceluzador, data={"txttlf": telefono}, headers=headers)
    data = response.json()
    if not data['error']:
        phone_info = json.loads(data['data'])

        if phone_info['fuente']:
            for fuente in phone_info['fuente']:
                print(f"     Nombre: {fuente['nombre']}")
        else:
            print("     Lo sentimos, No encontramos información en la fuente principal.")

        if phone_info['whatsapp']:
            if phone_info['whatsapp']['tiene_whatsapp'] :
                tiene_whatsapp = 'Si tiene' if phone_info['whatsapp']['tiene_whatsapp'] else 'No tiene'
                print(f"     WhatsApp: {tiene_whatsapp}")
                
                if phone_info['whatsapp']['foto_perfil']:
                    profile_pic_url = phone_info['whatsapp']['foto_perfil']
                    image_response = requests.get(profile_pic_url, stream=True)
                    image = Image.open(image_response.raw)

                    if not os.path.exists("./fotos"):
                        os.makedirs("./fotos")
                    ruta = f"./fotos/{telefono}.jpg"
                    image.save(ruta, format="JPEG")

                    whatsapp_status = json.loads(phone_info['whatsapp']['estado'])
                    print(f"     Estado: {whatsapp_status['status']}")
                    print(f"     Ultima Actualización: {whatsapp_status['setAt']}")
            else:
                print("     WhatsApp: No tiene")
        else:
            print("     WhatsApp: No tiene")

    else:
        print("     El número indicado es inválido, inténtalo nuevamente.")
        return None

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='OSINTchile', description='Búsqueda automática en fuentes abiertas (y no tan abiertas) de Chile')
    parser.add_argument('-telefono', type=str, nargs='?', help='Teléfono a buscar, con formato: 56999999999')

    parametros = parser.parse_args()

    if not parametros.telefono:
        parser.print_help()
    else:
        busqueda(parametros.telefono)
