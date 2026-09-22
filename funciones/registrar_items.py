import json


def registrar_libros():
    # 1. Cargar el inventario si el archivo ya existe para no perder datos
    try:
        with open("inventario.json", "r", encoding="utf-8") as archivo:
            inventario = json.load(archivo)
    except (FileNotFoundError, json.JSONDecodeError):
        inventario = {}

    while True:
        # Convertimos el código a string para mantener la consistencia con las llaves de JSON
        codigo = input("Ingrese el código del libro: ").strip()
        titulo = input("Ingrese el título del libro: ").strip()
        autor = input("Ingrese el autor del libro: ").strip()
        categoria = input("Ingrese la categoría del libro: ").strip()
        cantidad = int(
            input("Ingrese la cantidad de libros que va a añadir: ")
        )
        ubicacion = input("¿En qué ubicación va a poner los libros?: ").strip()

        # 2. Si el libro ya existe, actualizamos la cantidad en lugar de sobrescribir todo
        if codigo in inventario:
            inventario[codigo]["cantidad"] += cantidad
            print(
                f"\n El libro ya existía. Nueva cantidad total: {inventario[codigo]['cantidad']}"
            )
        else:
            inventario[codigo] = {
                "titulo": titulo,
                "autor": autor,
                "categoria": categoria,
                "cantidad": cantidad,
                "ubicacion": ubicacion,
            }
            print("\n Libro registrado con éxito.")

        respuesta = (
            input("\n¿Quiere añadir otro libro? (si/no): ").lower().strip()
        )
        if respuesta != "si":
            break

    # 3. Guardar en el archivo JSON al finalizar el bucle
    with open("inventario.json", "w", encoding="utf-8") as archivo:
        json.dump(inventario, archivo, indent=4, ensure_ascii=False)

    print("¡Inventario actualizado correctamente! Chao con adiós.")


registrar_libros()