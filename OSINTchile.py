import argparse
import sources.nombrerutyfirma as nrf
import sources.salud as salud
import sources.soap as soap
import sources.sii as sii
import sources.volanteomaleta as volanteomaleta
import sources.numverify as numverify

parser = argparse.ArgumentParser(prog='OSINTchile', description='Busqueda automatica en fuentes abiertas (y no tan abiertas) de chile')
parser.add_argument('-rut',  type=str, nargs='?', help='Rut de la persona a buscar, con formato: 11111111-1 ')
parser.add_argument('-patente', type=str, nargs='?', help='Patente del vehiculo a buscar, con formato: aabb11')
parser.add_argument('-telefono', type=str, nargs='?', help='telefono a buscar, con formato: 56999999999')

parametros = parser.parse_args()


if not(parametros.rut) and  not(parametros.patente) and  not(parametros.telefono):
    parser.print_help()

if parametros.rut:
    salud.busqueda(rut = parametros.rut)
    nrf.busqueda(rut = parametros.rut )
    sii.busqueda(rut = parametros.rut)
    volanteomaleta.busqueda(rut = parametros.rut)
if parametros.patente:
    print('---En Construccion, se aceptan contribuciones---')
    soap.busqueda(patente = parametros.patente)
if parametros.telefono:
    numverify.busqueda(telefono = parametros.telefono)
