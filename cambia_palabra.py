#!/usr/bin/python3

import sys

params = sys.argv

while len(params) < 4:
    if len(params) < 2:
        parametro = input("¿Cuál es la ruta del fichero? ")
        if len(parametro) == 0:
            continue
        params.append(parametro)

    if len(params) < 3:
        parametro = input("¿Cuál es la palabra original? ")
        if len(parametro) == 0:
            continue
        params.append(parametro)

    if len(params) < 4:
        parametro = input("¿Cuál es la palabra nueva? ")
        if len(parametro) == 0:
            continue
        params.append(parametro)
# params: [argumentos.py, fichero, original, nueva]

ruta = params[1]
palabra_original = params[2]
palabra_nueva = params[3]

fichero = open(ruta, "r")
texto = fichero.read()
fichero.close()

texto_final = texto.replace(palabra_original, palabra_nueva)

fichero = open(ruta, "w")
fichero.write(texto_final)
fichero.close()
