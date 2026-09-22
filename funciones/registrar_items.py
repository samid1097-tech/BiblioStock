import json


def registrar_libros():
    inventario={}
    while True:
        codigo=int(input("ingrese el codigo de el libro: "))
        titulo=input("ingrese el titulo de el libro: ")
        autor=input("ingrese el autor de el libro: ")
        categoria=input("ingrese la categoria de el libro: ")
        cantidad=int(input("ingrese la cantidad de libros que va a añadir: "))
        ubicacion=input("en que ubicacion va a poner los libros: ")

        inventario[codigo]={

            "titulo":titulo,
            "autor":autor,
            "categoria":categoria,
            "cantidad":cantidad,
            "ubicacion":ubicacion
        }

        with open("inventario.json","w",encoding="utf-8") as archivo:
            json.dump(inventario,archivo, indent=4,ensure_ascii=False)

        print("quiere añadir otro libro")
        respuesta=input().lower().strip()

        if respuesta!="si":
            print("bueno chao")
            break

registrar_libros()