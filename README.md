# osintChile
Busqueda automatica de informacion de personas en chile. Basado en web scrapping y algunas cosillas mas

Como lo Uso: 
  Sin parametros te muestra una ayuda

$ python3 OSINTchile.py
usage: OSINTchile [-h] [-rut [RUT]] [-patente [PATENTE]]
                  [-telefono [TELEFONO]]

Busqueda automatica en fuentes abiertas (y no tan abiertas) de chile

optional arguments:
  -h, --help            show this help message and exit
  -rut [RUT]            Rut de la persona a buscar, con formato: 11111111-1
  -patente [PATENTE]    Patente del vehiculo a buscar, con formato: aabb11
  -telefono [TELEFONO]  telefono a buscar, con formato: 56999999999


Ejemplos
$python3 OSINTchile.py -rut 3198442-4
$python3 OSINTchile.py -telefono 56955555555
$python3 OSINTchile.py -patente aabb11

