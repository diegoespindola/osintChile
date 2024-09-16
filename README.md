# OSINTChile v0.1 Beta

**Automatización de la búsqueda de información personal en Chile**  
*Basado en web scraping y otras técnicas avanzadas.*

## Descargo de Responsabilidad

Este script está diseñado exclusivamente con fines educativos y para generar conciencia sobre la privacidad de los datos en Chile.  
¿Realmente están protegidos los datos que entregamos a las empresas?

## ¿Cómo Usarlo?

Ejecutar el script sin parámetros mostrará una guía de ayuda:

```bash
$ python3 OSINTchile.py
```

### Uso:
```bash
$ python3 OSINTchile.py [-h] [-rut [RUT]] [-patente [PATENTE]] [-telefono [TELEFONO]]
```

**Descripción:**  
Automatiza la búsqueda de información en fuentes abiertas (y algunas menos abiertas) de Chile.

**Argumentos Opcionales:**

- `-h, --help`  
  Muestra este mensaje de ayuda y termina la ejecución.

- `-rut [RUT]`  
  Busca información de una persona utilizando su RUT. Formato: `11111111-1`.

- `-patente [PATENTE]`  
  Busca información de un vehículo utilizando su patente. Formato: `aabb11`.

- `-telefono [TELEFONO]`  
  Busca información asociada a un número de teléfono. Formato: `56999999999`.

### Ejemplos de Uso:

```bash
$ python3 OSINTchile.py -rut 3198442-4
$ python3 OSINTchile.py -telefono 56955555555
$ python3 OSINTchile.py -patente aabb11
```
