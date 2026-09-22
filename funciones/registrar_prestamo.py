import json

def registrar_prestamo():
    try:
        with open("inventario.json","r") as archivo:
            libros=json.load(archivo)
            print("libos con los que contamos disponibilidad:")
            for libro in libros:
                print(f"codigo{[codigo]}")
    except FileNotFoundError:
        print ("no contamos con libros disponible")

registrar_prestamo()
