import sys 
from bs4 import BeautifulSoup
import requests
datos = requests.get("http://www.sismologia.cl/links/ultimos_sismos.html")

soup = BeautifulSoup(datos.text, "html.parser")
cont=0

for row in soup.table.tbody("tr"):
    if cont==0:
        cont+=1
    else:
        raw_fecha = row("td")[0]
        raw_intencidad = row("td")[5]
        raw_ubicacion = row("td")[7]

        str_fecha = raw_fecha.text
        str_intencidad = raw_intencidad.text
        str_ubicacion = raw_ubicacion.text
        print("Se registro un sismo con fecha local " + str_fecha + " de magnitud " + str_intencidad + " a " + str_ubicacion)
    