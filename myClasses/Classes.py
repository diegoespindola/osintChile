import json

class Exporter:
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=False, indent=4, ensure_ascii=False).encode('utf8').decode()

class Email(Exporter):

    def __init__(self, address = '', Source = ''):
        self.Address = address
        self.Source = Source


class Telefono(Exporter):

    def __init__(self, number = '', Source = ''):
        self.Numero = number
        self.Pais = ''
        self.Compañia = ''
        self.Tipo = ''
        self.Source = Source

class Motores(Exporter):

    def __init__(self, Placa = '', Source = ''):
        self.Placa = Placa
        self.Source = Source

class Direccion(Exporter):
    def __init__(self, Direccion, Source = ''):
        self.Direccion = Direccion
        self.Calle = ''
        self.Numero = ''
        self.Ciudad = ''
        self.Comuna = ''
        self.Source = Source

class DatosPersonales(Exporter):
    def __init__(self, Source = ''):
        self.PrimerNombre = ''
        self.SegundoNombre = ''
        self.ApellidoPaterno = ''
        self.ApellidoMaterno = ''
        self.RutFormateado = ''
        self.NombreCompleto = ''
        self.Sexo = ''
        self.Source = Source


class Objetivo(Exporter):
    def __init__(self, Rut):
        self.Rut = Rut
        self.DatosPersonales = []
        self.Telefonos = []
        self.Correos = []
        self.Autos = []
        self.Direcciones = []

