# CambiarPalabras

Comando creado en Python que permite cambiar una palabra por otra en un archivo de texto.

## Forma de uso:

```
python cambia_palabra.py archivo original nueva
```


## Programas como comando del shell

**Unix/Linux/Mac**

Agregar al principio, en la primera línea

```
#!/usr/bin/python3
```

(podéis saber dónde está el ejecutable de python con el comando `which python`)

y basta con poner un acceso directo (symbolic link) en `/usr/bin` (o copiarlo directamente).

**Windows**

1. Crear un archivo `.cmd` que llame a `python <ruta del script>`
2. Copiar el archivo `.cmd` a una carpeta dentro del path (c:\windows, c:\windows\system32)
