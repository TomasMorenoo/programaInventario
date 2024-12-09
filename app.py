# Lista para almacenar los productos
productos = []

# Función para agregar un producto
def agregar_producto():
    print("\n----------------------------------------")
    print("----------- Agregar producto -----------")
    print("----------------------------------------")
    nombre = input("--- Nombre: ")
    precio = float(input("--- Precio: $"))
    cantidad = float(input("--- Cantidad: "))
    print("----------------------------------------")
    producto = {
        "nombre": nombre,
        "cantidad": cantidad
    }
    productos.append(producto)
    print("\n----------------------------------------")
    print("--- Producto agregado correctamente! ---")
    print("----------------------------------------\n")

    print("\n----------------------------------------")
    print("----- ¿Deseas agregar otro producto? ---")
    print("--- 1. Sí ------------------------------")
    print("--- 2. No, regresar al menú ------------")
    print("--- 3. Salir del sistema ---------------")
    print("----------------------------------------")

    respuesta = input("--- Opción: ")
    print("----------------------------------------\n")

    if respuesta == "1":
        agregar_producto()
    elif respuesta == "3":
        print("\n-------------------------------------------------")
        print("--Gracias por utilizar el sistema de inventario--")
        print("-------------------------------------------------\n")
        return False 
    else:
        return True  

# Función para ver los productos
def ver_productos():
    print("\n----------------------------------------")
    print("---------- Lista de productos ----------")
    print("----------------------------------------\n")
    if len(productos) == 0:
        print("----------------------------------------")
        print("-- No hay productos en el registrados --")
        print("----------------------------------------")
    else:
        print("----------------------------------------")
        for producto in productos:
            print(f"Producto: {producto['nombre']},Precio: ${producto['precio']},Cantidad: {producto['cantidad']}")
        print("----------------------------------------\n")

# Función principal para el sistema de inventario (NO ELIMINAR)
def main():
    while True:
        print("\n----------------------------------------")
        print("------------ Menú Principal ------------")
        print("----------------------------------------")
        print("--- Por favor selecciona una opción: ---")
        print("----------------------------------------")
        print("--- 1. Agregar producto ----------------")
        print("--- 2. Ver productos -------------------")
        print("--- 3. Salir del sistema----------------")
        print("----------------------------------------")
        opcion = input("--- Opción: ")
        print("----------------------------------------")
        
        if opcion == "1":
            if not agregar_producto():
                break 
        elif opcion == "2":
            ver_productos()
        elif opcion == "3":
            print()
            print("----------------------------------------")
            print("--------- Gracias por utilizar ---------")
            print("------- el sistema de inventario -------")
            print("----------------------------------------")
            break
        else:
            print("Opción inválida, prueba de nuevo")

# Ejecución de la función main() - (NO ELIMINAR)
if __name__ == "__main__":
    print()
    print("----------------------------------------")
    print("- Bienvenido al sistema de inventario! -")
    print("----------------------------------------")
    main()
