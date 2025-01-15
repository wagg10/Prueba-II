
inventario = {
    1: {"nombre": "Ropa", "cantidad": 100 },
    2: {"nombre": "Calzado", "cantidad": 200},
}

def consultar_producto(id_producto):
    """Consulta un producto por su ID."""
    if not isinstance(id_producto, int) or id_producto <= 0:
        return {"error": "El ID del producto debe ser un número entero positivo."}
    
    producto = inventario.get(id_producto)
    if producto is None:
        return {"error": "Producto no encontrado."}
    
    return {"nombre": producto["nombre"], "cantidad": producto["cantidad"]}


def agregar_producto(id_producto, cantidad):
    """Agrega un producto nuevo o suma cantidad a un producto existente."""
    if not isinstance(id_producto, int) or id_producto <= 0:
        return {"error": "El ID del producto debe ser un número entero positivo."}
    if not isinstance(cantidad, int) or cantidad <= 0:
        return {"error": "La cantidad debe ser un número entero positivo."}
    
    if id_producto in inventario:
        # Si el producto ya existe, actualiza la cantidad
        inventario[id_producto]["cantidad"] += cantidad
        return {"mensaje": f"Cantidad actualizada. Nuevo stock: {inventario[id_producto]['cantidad']}"}
    else:
        # Si el producto no existe, lo crea
        inventario[id_producto] = {"nombre": f"Producto {id_producto}", "cantidad": cantidad}
        return {"mensaje": f"Producto creado con éxito. ID: {id_producto}, Cantidad: {cantidad}"}


def actualizar_stock(id_producto, nueva_cantidad):
    """Actualiza el stock de un producto."""
    # Precondiciones (contrato)
    assert isinstance(id_producto, int) and id_producto > 0, "El ID del producto debe ser un entero positivo."
    assert isinstance(nueva_cantidad, int) and nueva_cantidad >= 0, "La nueva cantidad debe ser un número entero no negativo."
    
    # Verifica si el producto existe
    if id_producto not in inventario:
        raise ValueError("Producto no encontrado. No se puede actualizar el stock.")
    
    # Actualización del stock
    inventario[id_producto]["cantidad"] = nueva_cantidad
    return {"mensaje": f"Stock actualizado. Nuevo stock: {nueva_cantidad}"}
