import json

def registrar_prestamo():
    try:
        with open("inventario.json","r") as archivo:
            libros = json.load(archivo)
            print(libros)
            print("libos con los que contamos:")
            for x in libros:
                print(f"codigo: {x['codigo']}")
                print(f"titulo: {x['titulo']}")
                print(f"autor: {x['autor']}")
                print(f"cantidad_disponible: {x['cantidad_disponible']}")
        libro_presta = int(input("ingrese el codigo del libro que desea prestar: "))
        for x in libros:
            if libro_presta == x['codigo']:
                 if x['cantidad_disponible'] >0:
                    x ['cantidad_disponible'] = -1
                    with open ("inventario.json","w") as prestamos:
                        l_prestamos = json.dump(libros,prestamos,indent=4)
                    print("prestamo realizado con exito")


    except FileNotFoundError:
            print ("no contamos con libros disponible")
registrar_prestamo()
