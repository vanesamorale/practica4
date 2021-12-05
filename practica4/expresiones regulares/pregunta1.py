import re

texto = "En esta cadena se encuentra una palabra mágica"

re.search('mágica', texto)
re.search('hola', texto)
palabra = "mágica"
encontrado = re.search(palabra,  texto)

if encontrado:
    print("Se ha encontrado la palabra:", palabra)
else:
    print("No se ha encontrado la palabra:", palabra)