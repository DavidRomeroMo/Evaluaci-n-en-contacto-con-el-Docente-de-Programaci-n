# ------------------------------------------------------------
# PROYECTO FINAL: SISTEMA DE CONTROL DE INVENTARIO PARA TIENDA
# Materia: Lógica de Programación
# Este programa permite administrar el inventario de una tienda,
# controlar productos, ventas, stock y fechas de caducidad.
# ------------------------------------------------------------

# Importamos datetime para obtener la fecha actual y validar fechas de caducidad de los productos
from datetime import datetime, date


# Creamos una lista vacía donde se almacenarán todos los productos
inventario = []


# FUNCIÓN PARA VALIDAR FECHAS
def ingresar_fecha():
    # Este ciclo se repite hasta que el usuario ingrese una fecha válida
    while True:
        # Se solicita la fecha en formato año-mes-día
        fecha_texto = input("Ingrese la fecha de caducidad del producto (AAAA-MM-DD): ")

        try:
            # Aqui convierto el texto ingresado a tipo fecha
            fecha = datetime.strptime(fecha_texto, "%Y-%m-%d").date()

            # Retornamos la fecha validada
            return fecha

        except ValueError:
            # Si el formato está mal, se muestra un mensaje de error
            print("Error: La fecha debe tener el formato AAAA-MM-DD. Ejemplo: 2026-12-31")


# FUNCIÓN PARA AGREGAR PRODUCTOS AL INVENTARIO
def agregar_producto():
    # Mostramos el título de la opción
    print("\n--- AGREGAR PRODUCTO ---")

    # Se solicita el nombre del producto
    nombre = input("Ingrese el nombre del producto: ").lower()

    # Se verifica si el producto ya existe en el inventario
    for producto in inventario:
        if producto["nombre"] == nombre:
            print("Este producto ya existe en el inventario.")
            return

    # Se valida que el precio sea un número positivo
    while True:
        try:
            precio = float(input("Ingrese el precio del producto: "))

            if precio <= 0:
                print("El precio debe ser mayor que cero.")
            else:
                break

        except ValueError:
            print("Error: Ingrese un valor numérico válido para el precio.")

    # Se valida que la cantidad sea un número entero positivo o cero
    while True:
        try:
            cantidad = int(input("Ingrese la cantidad en stock: "))

            if cantidad < 0:
                print("La cantidad no puede ser negativa.")
            else:
                break

        except ValueError:
            print("Error: Ingrese un número entero válido para la cantidad.")

    # Se solicita la fecha de caducidad usando la función de validación
    fecha_caducidad = ingresar_fecha()

    # Se crea un diccionario con la información del producto
    producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad,
        "fecha_caducidad": fecha_caducidad
    }

    # Se agrega el producto a la lista inventario
    inventario.append(producto)

    # Se muestra el mensaje de confirmación
    print("Producto agregado correctamente al inventario.")


# FUNCIÓN PARA MOSTRAR TODO EL INVENTARIO
def mostrar_inventario():
    # Se muestra el título de la opción
    print("\n--- INVENTARIO COMPLETO ---")

    # Se verifica si el inventario está vacío
    if len(inventario) == 0:
        print("El inventario está vacío.")
        return

    # Recorremos la lista de productos
    for i, producto in enumerate(inventario, start=1):
        # Se muestra los datos de cada producto
        print(f"\nProducto #{i}")
        print(f"Nombre: {producto['nombre']}")
        print(f"Precio: ${producto['precio']:.2f}")
        print(f"Cantidad en stock: {producto['cantidad']}")
        print(f"Fecha de caducidad: {producto['fecha_caducidad']}")


# FUNCIÓN PARA VENDER PRODUCTOS
def vender_producto():
    # Se muestra el título de la opción
    print("\n--- VENDER PRODUCTO ---")

    # Se verifica si existen productos en el inventario
    if len(inventario) == 0:
        print("No hay productos registrados para vender.")
        return

    # Se solicita el nombre del producto a vender
    nombre = input("Ingrese el nombre del producto a vender: ").lower()

    # Se recorre el inventario para buscar el producto
    for producto in inventario:
        if producto["nombre"] == nombre:

            # Se valida que la cantidad a vender sea correcta
            while True:
                try:
                    cantidad_vender = int(input("Ingrese la cantidad a vender: "))

                    if cantidad_vender <= 0:
                        print("La cantidad a vender debe ser mayor que cero.")

                    elif cantidad_vender > producto["cantidad"]:
                        print("No hay suficiente stock disponible.")
                        print(f"Stock actual: {producto['cantidad']}")

                    else:
                        break

                except ValueError:
                    print("Error: Ingrese un número entero válido.")

            # Se resta la cantidad vendida del stock actual
            producto["cantidad"] -= cantidad_vender

            # Se calcula el total de la venta
            total = cantidad_vender * producto["precio"]

            # Se muestra la información de la venta
            print("Venta realizada correctamente.")
            print(f"Total de la venta: ${total:.2f}")
            print(f"Stock restante: {producto['cantidad']}")

            return

    # Si no se encontró el producto, Se muestra un mensaje
    print("Producto no encontrado en el inventario.")


# FUNCIÓN PARA ACTUALIZAR EL STOCK DE UN PRODUCTO
def actualizar_stock():
    # Se muestra el título de la opción
    print("\n--- ACTUALIZAR STOCK ---")

    # Se verifica si hay productos registrados
    if len(inventario) == 0:
        print("No hay productos registrados.")
        return

    # Se solicita el nombre del producto
    nombre = input("Ingrese el nombre del producto a actualizar: ").lower()

    # Se busca el producto dentro del inventario
    for producto in inventario:
        if producto["nombre"] == nombre:

            # Se valida la nueva cantidad de stock
            while True:
                try:
                    nueva_cantidad = int(input("Ingrese la nueva cantidad en stock: "))

                    if nueva_cantidad < 0:
                        print("La cantidad no puede ser negativa.")
                    else:
                        break

                except ValueError:
                    print("Error: Ingrese un número entero válido.")

            # Se actualiza la cantidad del producto
            producto["cantidad"] = nueva_cantidad

            # Se muestra mensaje de confirmación
            print("Stock actualizado correctamente.")
            return

    # Si el producto no existe, mostramos mensaje
    print("Producto no encontrado.")


# FUNCIÓN PARA MOSTRAR PRODUCTOS AGOTADOS
def mostrar_productos_agotados():
    # Se muestra el título de la opción
    print("\n--- PRODUCTOS AGOTADOS ---")

    # Se crea una variable para saber si se encontró algún producto agotado
    encontrados = False

    # Se recorre el inventario
    for producto in inventario:
        # Verificamos si la cantidad es igual a cero
        if producto["cantidad"] == 0:
            print(f"Producto agotado: {producto['nombre']}")
            encontrados = True

    # Si no se encontró ningún producto agotado
    if not encontrados:
        print("No hay productos agotados.")


# FUNCIÓN PARA MOSTRAR PRODUCTOS CERCA DE CADUCAR
def mostrar_productos_por_caducar():
    # Se muestra el título de la opción
    print("\n--- PRODUCTOS CERCANOS A CADUCAR ---")

    # Se obtiene la fecha actual del sistema
    fecha_actual = date.today()

    # Se define cuántos días se consideran cercanos a caducar
    dias_limite = 7

    # Variable para verificar si existen productos próximos a caducar
    encontrados = False

    # Se recorren todos los productos del inventario
    for producto in inventario:
        # Se calcula cuántos días faltan para que caduque el producto
        dias_restantes = (producto["fecha_caducidad"] - fecha_actual).days

        # Si el producto ya caducó
        if dias_restantes < 0:
            print(f"{producto['nombre']} ya está caducado. Fecha: {producto['fecha_caducidad']}")
            encontrados = True

        # Si el producto caduca dentro del límite establecido
        elif dias_restantes <= dias_limite:
            print(f"{producto['nombre']} caduca en {dias_restantes} días. Fecha: {producto['fecha_caducidad']}")
            encontrados = True

    # Si no hay productos cercanos a caducar
    if not encontrados:
        print("No hay productos cercanos a caducar.")


# FUNCIÓN PARA BUSCAR UN PRODUCTO
def buscar_producto():
    # Se muestra el título de la opción
    print("\n--- BUSCAR PRODUCTO ---")

    # Se verifica si el inventario está vacío
    if len(inventario) == 0:
        print("El inventario está vacío.")
        return

    # Se solicita el nombre del producto
    nombre = input("Ingrese el nombre del producto que desea buscar: ").lower()

    # Se recorre el inventario para buscar coincidencias
    for producto in inventario:
        if producto["nombre"] == nombre:
            print("\nProducto encontrado:")
            print(f"Nombre: {producto['nombre']}")
            print(f"Precio: ${producto['precio']:.2f}")
            print(f"Cantidad en stock: {producto['cantidad']}")
            print(f"Fecha de caducidad: {producto['fecha_caducidad']}")
            return

    # Si no se encuentra el producto
    print("Producto no encontrado.")


# FUNCIÓN PARA MOSTRAR EL MENÚ PRINCIPAL
def mostrar_menu():
    # Se muestran todas las opciones disponibles para el usuario
    print("\n====================================")
    print(" SISTEMA DE CONTROL DE INVENTARIO")
    print("====================================")
    print("1. Agregar producto")
    print("2. Mostrar inventario")
    print("3. Vender producto")
    print("4. Actualizar stock")
    print("5. Mostrar productos agotados")
    print("6. Mostrar productos cercanos a caducar")
    print("7. Buscar producto")
    print("8. Salir")


# FUNCIÓN PRINCIPAL DEL PROGRAMA
def main():
    # Este ciclo permite que el menú se repita hasta que el usuario decida salir
    while True:
        # Se llama a la función que muestra el menú
        mostrar_menu()

        # Se solicita la opción al usuario
        opcion = input("Seleccione una opción: ")

        # Se evalúa la opción ingresada usando condicionales
        if opcion == "1":
            agregar_producto()

        elif opcion == "2":
            mostrar_inventario()

        elif opcion == "3":
            vender_producto()

        elif opcion == "4":
            actualizar_stock()

        elif opcion == "5":
            mostrar_productos_agotados()

        elif opcion == "6":
            mostrar_productos_por_caducar()

        elif opcion == "7":
            buscar_producto()

        elif opcion == "8":
            print("Gracias por usar el sistema de inventario.")
            print("Programa finalizado.")
            break

        else:
            # Si el usuario ingresa una opción incorrecta
            print("Opción no válida. Intente nuevamente.")


# INICIO DEL PROGRAMA

# Esta condición permite ejecutar el programa desde este archivo principal
if __name__ == "__main__":
    main()