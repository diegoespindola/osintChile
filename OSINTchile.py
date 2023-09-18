import argparse
import sources.nombrerutyfirma as nrf
import sources.salud as salud
import sources.soap as soap
import sources.sii as sii
import sources.volanteomaleta as volanteomaleta
import sources.numverify as numverify
import sources.masterchileapkBday as mchaBday
import sources.celuzador as celuzador
import sources.rutificador as rutificador
import sources.indisa as indisa

parser = argparse.ArgumentParser(prog='OSINTchile', description='Búsqueda automática en fuentes abiertas (y no tan abiertas) de Chile')
parser.add_argument('-rut', type=str, nargs='?', help='RUT de la persona a buscar, con formato: 11111111-1')
parser.add_argument('-patente', type=str, nargs='?', help='Patente del vehículo a buscar, con formato: aabb11')
parser.add_argument('-telefono', type=str, nargs='?', help='Teléfono a buscar, con formato: 56999999999')
parser.add_argument('-nombre', action='store_true', help='Buscar información por nombre')

parametros = parser.parse_args()

if not (parametros.rut) and not (parametros.patente) and not (parametros.telefono) and not (parametros.nombre):
    parser.print_help()

if parametros.rut:
    salud.busqueda(rut=parametros.rut)
    nrf.busqueda(rut=parametros.rut)
    sii.busqueda(rut=parametros.rut)
    volanteomaleta.busqueda(rut=parametros.rut)
    mchaBday.busqueda(rut=parametros.rut)
    indisa.busqueda(rut=parametros.rut)

if parametros.patente:
    print('---En Construcción, se aceptan contribuciones---')
    soap.busqueda(patente=parametros.patente)
    volanteomaleta.busqueda(patente=parametros.patente)

if parametros.telefono:
    print('---En Construcción, se aceptan contribuciones---')
    numverify.busqueda(telefono=parametros.telefono)
    celuzador.busqueda(telefono=parametros.telefono)

# Nuevo bloque para el argumento '-nombre'
if parametros.nombre:
    rutificador.buscar_info_por_nombre(parametros.nombre)
