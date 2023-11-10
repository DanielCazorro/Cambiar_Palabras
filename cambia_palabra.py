import sys

def main():
    # Verificar que se proporcionen los argumentos necesarios
    if len(sys.argv) != 4:
        print("Uso: python cambia_palabra.py archivo original nueva")
        return

    # Obtener los argumentos
    ruta = sys.argv[1]
    palabra_original = sys.argv[2]
    palabra_nueva = sys.argv[3]

    try:
        # Abrir el archivo en modo lectura
        with open(ruta, "r") as fichero:
            texto = fichero.read()

        # Reemplazar la palabra original con la nueva
        texto_final = texto.replace(palabra_original, palabra_nueva)

        # Abrir el archivo en modo escritura y escribir el texto modificado
        with open(ruta, "w") as fichero:
            fichero.write(texto_final)

        print(f"Palabra '{palabra_original}' cambiada por '{palabra_nueva}' en '{ruta}'.")
    except FileNotFoundError:
        print(f"No se encuentra el archivo: {ruta}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
