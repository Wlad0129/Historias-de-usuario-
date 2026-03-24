# Lista global para almacenar los productos del inventario
inventario = []

def agregar_producto():
    """
    Solicita al usuario los datos de un nuevo producto,
    valida que el precio y la cantidad sean números,
    y lo agrega a la lista de inventario como un diccionario.
    """
    print("\n--- Agregar Nuevo Producto ---")
    nombre = input("Ingresa el nombre del producto: ")
    
    # Bucle para asegurar que el usuario ingrese un precio numérico válido
    while True:
        try:
            # Usamos float por si el precio tiene decimales
            precio = float(input(f"Ingresa el precio de '{nombre}': "))
            if precio < 0:
                print("✘ El precio no puede ser negativo. Intenta de nuevo.")
            else:
                break # Salimos del bucle si el dato es correcto
        except ValueError:
            print("✘ Por favor, ingresa un número válido para el precio (ej. 500 o 500.50).")
            
    # Bucle para asegurar que el usuario ingrese una cantidad entera válida
    while True:
        try:
            # Usamos int porque la cantidad de artículos suele ser entera
            cantidad = int(input(f"Ingresa la cantidad de '{nombre}': "))
            if cantidad < 0:
                print("✘ La cantidad no puede ser negativa. Intenta de nuevo.")
            else:
                break # Salimos del bucle si el dato es correcto
        except ValueError:
            print("✘ Por favor, ingresa un número entero válido para la cantidad (ej. 3).")

    # Guardamos los datos recibidos en un diccionario
    producto = {
        "nombre": nombre, 
        "precio": precio, 
        "cantidad": cantidad
    }
    
    # Agregamos el diccionario a nuestra lista de inventario
    inventario.append(producto)
    print(f"\n✔ ¡Producto '{nombre}' agregado exitosamente al inventario!")

def mostrar_inventario():
    """
    Recorre la lista de inventario y muestra cada producto.
    Si el inventario está vacío, muestra un mensaje indicándolo.
    """
    # Verificamos si la lista está vacía
    if len(inventario) == 0:
        print("\nℹ El inventario está vacío. No hay productos para mostrar.")
    else:
        print("\n--- Lista de Productos en el Inventario ---")
        # Usamos un bucle for para recorrer cada diccionario en la lista
        for producto in inventario:
            # Formateando la salida para que sea clara y siga el requerimiento
            print(f"Producto: {producto['nombre']} | Precio: {producto['precio']} | Cantidad: {producto['cantidad']}")
        print("-------------------------------------------")

def calcular_estadisticas():
    """
    Calcula y muestra el valor total del inventario (precio * cantidad)
    y la cantidad total de artículos registrados.
    """
    if len(inventario) == 0:
        print("\nℹ El inventario está vacío. No hay estadísticas para calcular.")
        # Usamos return para salir de la función tempranamente
        return

    valor_total = 0
    cantidad_total = 0

    # Recorremos el inventario iterando sobre cada producto
    for producto in inventario:
        # Sumatoria de (precio x cantidad) para el valor del inventario
        valor_total += producto["precio"] * producto["cantidad"]
        # Sumatoria de la cantidad total de todos los productos
        cantidad_total += producto["cantidad"]

    print("\n--- Estadísticas Básicas ---")
    print(f"▶ Cantidad total de productos registrados: {cantidad_total}")
    print(f"▶ Valor total del inventario: {valor_total}")
    print("----------------------------")

def iniciar_programa():
    """
    Función principal que muestra el menú y maneja el bucle
    hasta que el usuario elija salir.
    """
    # Bucle while que mantendrá el menú activo hasta que le digamos que se detenga
    while True:
        print("\n====== MENÚ PRINCIPAL ======")
        print("1. Agregar producto")
        print("2. Mostrar inventario")
        print("3. Calcular estadísticas")
        print("4. Salir")
        print("============================")
        
        # Le pedimos la opción al usuario
        opcion = input("Elige una opción (1-4): ")

        # Validamos usando condicionales if, elif y else (Requerimiento 1)
        if opcion == '1':
            agregar_producto()
        elif opcion == '2':
            mostrar_inventario()
        elif opcion == '3':
            calcular_estadisticas()
        elif opcion == '4':
            print("\n¡Gracias por usar el sistema de inventario! Hasta luego. 👋")
            break  # Con "break" rompemos el ciclo while y terminamos el programa
        else:
            # Else actúa como nuestro control si eligen algo que no es 1, 2, 3 o 4
            print("\n✘ Opción inválida. Por favor, ingresa un número del 1 al 4.")

# Este bloque verifica si el archivo se está ejecutando directamente y llama a la función principal
if __name__ == "__main__":
    iniciar_programa()
