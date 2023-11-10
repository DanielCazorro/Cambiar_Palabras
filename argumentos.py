import sys

def main():
    # Obtener los argumentos
    params = sys.argv

    # Pedir la ruta del archivo si no se proporciona
    while len(params) < 4:
        if len(params) < 2:
            parametro = input("¿Cuál es la ruta del fichero? ")
            if len(parametro) == 0:
                continue
            params.append(parametro)

        # Pedir la palabra original si no se proporciona
        if len(params) < 3:
            parametro = input("¿Cuál es la palabra original? ")
            if len(parametro) == 0:
                continue
            params.append(parametro)

        # Pedir la palabra nueva si no se proporciona
        if len(params) < 4:
            parametro = input("¿Cuál es la palabra nueva? ")
            if len(parametro) == 0:
                continue
            params.append(parametro)

    # Mostrar los parámetros
    print(f"Parámetros: {params}")

if __name__ == "__main__":
    main()
