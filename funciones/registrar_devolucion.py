def registrar_devolucion(inventario):
    """
    Registra la devolución de un ítem en el inventario de BiblioStock.
    Valida la existencia del ítem y comprueba que no se devuelvan más unidades
    del total registrado.
    """
    codigo = input("Ingrese el código del ítem a devolver: ").strip().upper()
    
    # Buscar el ítem dentro de la lista del inventario
    item_encontrado = None
    for item in inventario:
        if item.get("codigo") == codigo:
            item_encontrado = item
            break
            
    if not item_encontrado:
        print(f"Error: No se encontró ningún ítem con el código '{codigo}'.")
        return
        
    # Comprobar que la devolución sea válida
    if item_encontrado["cantidad_disponible"] >= item_encontrado["cantidad_total"]:
        print(f"Error: La cantidad disponible ({item_encontrado['cantidad_disponible']}) ya es igual al total de unidades ({item_encontrado['cantidad_total']}). No hay préstamos pendientes para este ítem.")
        return
        
    # Aumentar la cantidad disponible
    item_encontrado["cantidad_disponible"] += 1
    
    print(f"Devolución registrada exitosamente para '{item_encontrado['titulo']}'.")
    print(f"Disponibles actualmente: {item_encontrado['cantidad_disponible']}/{item_encontrado['cantidad_total']}")