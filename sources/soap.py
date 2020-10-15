import urllib

if __name__ == "__main__":
    print('Esto no se ejecuta solo, es para ser llamado desde el programa principal')


def busqueda(patente):
    busquedaSoapOK(patente)


def busquedaSoapOK(patente):

    urlTipoVehiculo = 'https://www.soapok.cl/seguros-online/SOAP/busca_tipo_veh.php'
    parametrosTIpoVehiculo = {"patente":patente}
    data = urllib.parse.urlencode(parametrosTIpoVehiculo).encode('ascii')

    response = urllib.request.urlopen(urllib.parse.unquote(urlTipoVehiculo), data).read().decode()
    tipovehiculo = response.split(';')[3]
    print('--==<Datos desde SOAP OK>==--')
    print('Tipo de Vehiculo:', tipovehiculo)
