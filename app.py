#IMPORTACIONES
import colorama # Importamos la librería colorama
import sqlite3 as sql

#FUNCIONES
# Creacion de database y tabla

def createDB():
    conn = sql.connect('inventario.db') # Creamos la conexión a la base de datos
    conn.commit() # Guardamos los cambios
    conn.close() # Cerramos la conexión

def createTable():
    conn = sql.connect('inventario.db') # Creamos la conexión a la base de datos
    cursor = conn.cursor() # Creamos el cursor
    cursor.execute(
        """CREATE TABLE productos(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            descripcion TEXT,
            precio REAL NOT NULL,
            cantidad INTEGER NOT NULL,
            categoria TEXT
        )"""
    )
    conn.commit
    conn.close()

#FUNCIONES PRINCIPALES

def agregarProducto():
    print(colorama.Fore.RED)

    nombre= input("Ingrese el nombre del producto: ")
    descripcion = input("Ingrese la descripción del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    cantidad = int(input("Ingrese la cantidad del producto: "))
    categoria = input("Ingrese la categoría del producto: ")

    print(colorama.Fore.RESET)
    print(colorama.Fore.YELLOW + "Agregando producto...")
    print(colorama.Fore.RESET)

    conn = sql.connect('inventario.db')
    cursor = conn.cursor() 
    instruccion = f"INSERT INTO productos (nombre, descripcion, precio, cantidad, categoria) VALUES (?, ?, ?, ?, ?) "
    cursor.execute(instruccion, (nombre, descripcion, precio, cantidad, categoria))

    print(colorama.Fore.GREEN + f"Producto '{nombre}' agregado con éxito")
    print(colorama.Fore.RESET)

    conn.commit()
    conn.close()


def leerInventario():
    conn = sql.connect('inventario.db') 
    cursor = conn.cursor()
    instruccion = f"SELECT * FROM productos"
    cursor.execute(instruccion)
    datos = cursor.fetchall()
    conn.commit()
    conn.close()

    print("Inventario actual:")
    print("-" * 50)
    for fila in datos:
        id, nombre, descripcion, precio, cantidad, categoria = fila
        print(f"ID: {id}")
        print(f"Nombre: {nombre}")
        print(f"Descripción: {descripcion}")
        print(f"Precio: ${precio:.2f}")
        print(f"Cantidad: {cantidad}")
        print(f"Categoría: {categoria}")
        print("-" * 50)


def identificarProducto():
    while True:
        print(colorama.Fore.RED)
        idProducto = int(input("Ingrese el ID del producto: ")) # Solicitamos el ID del producto
        # Mostramos el producto seleccionado
        conn = sql.connect('inventario.db')
        cursor = conn.cursor() 
        instruccion = f"SELECT nombre, cantidad, precio, categoria FROM productos WHERE id = ? "
        cursor.execute(instruccion, (idProducto,))
        datos = cursor.fetchone()
        conn.close()
    
        if datos:
            nombre, cantidad, precio, categoria = datos  # Desempaquetamos los valores
            print(colorama.Fore.YELLOW + f"El producto seleccionado es: {nombre}")
            print(colorama.Fore.YELLOW + f"Cantidad actual: {cantidad}")
            print(colorama.Fore.YELLOW + f"Precio: ${precio:.2f}")
            print(colorama.Fore.YELLOW + f"Categoría: {categoria}")
            print(colorama.Fore.RESET)

            print(colorama.Fore.CYAN + "Este es el producto que usted esta buscando?")
            print( "1. Si")
            print("2. No")
            opcion = int(input(colorama.Fore.RED + "Seleccione una opción: "))
            if opcion == 1:
                return nombre, cantidad, precio, categoria, idProducto # Retornamos los valores
            elif opcion == 2:
                print(colorama.Fore.GREEN + "Saliendo...")
                return 
        else:
            print(colorama.Fore.RED + "El producto con ese ID no existe.")


def editarCantidad():
    nombre, cantidad, precio, categoria, idProducto = identificarProducto()

    nuevaCantidad = int(input("Ingrese la nueva cantidad del producto: ")) # Solicitamos la nueva cantidad del producto
    print(colorama.Fore.RESET)
    print(colorama.Fore.YELLOW + "Editando producto...")

    conn = sql.connect('inventario.db') # Creamos la conexión a la base de datos
    cursor = conn.cursor() # Creamos el cursor
    instruccion = f"UPDATE productos SET cantidad = {nuevaCantidad}  WHERE id = {idProducto}" 
    cursor.execute(instruccion)

    print(colorama.Fore.GREEN + f"{nombre} paso de tener {cantidad} unidades a tener {nuevaCantidad} unidades")
    conn.commit()
    conn.close()

def eliminarProducto():
    nombre, cantidad, precio, categoria, idProducto = identificarProducto()
    print()
    print(colorama.Fore.RED + "¿Está seguro que desea eliminar este producto?: ")
    print("1. Si")
    print("2. No")
    opcion = int(input(colorama.Fore.RED + "Seleccione una opción: "))

    while opcion != 1 and opcion != 2:
        print()
        print(colorama.Fore.RED + "Opción inválida. Intente de nuevo.")
        print(colorama.Fore.RESET)
        print(colorama.Fore.RED + "¿Está seguro que desea eliminar este producto?: ")
        print("1. Si")
        print("2. No")
        opcion = int(input(colorama.Fore.RED + "Seleccione una opción: "))

    if opcion == 1:
        print(colorama.Fore.RESET)
        print(colorama.Fore.YELLOW + "Eliminando producto...")
        print(colorama.Fore.RESET)
        conn = sql.connect('inventario.db') # Creamos la conexión a la base de datos
        cursor = conn.cursor() # Creamos el cursor
        instruccion = f"DELETE FROM productos WHERE id = ?" 
        cursor.execute(instruccion, (idProducto,))
        conn.commit()
        conn.close()
        print(colorama.Fore.GREEN + f"Producto '{nombre}' eliminado con éxito")
        print(colorama.Fore.RESET)
    elif opcion == 2:
        print(colorama.Fore.GREEN + "Saliendo...")
        print(colorama.Fore.RESET)
    else:
        print(colorama.Fore.RED + "Opción inválida. Intente de nuevo.")
        print(colorama.Fore.RESET)

def reporteStockBajo():
    conn = sql.connect('inventario.db') # Creamos la conexión a la base de datos
    cursor = conn.cursor() # Creamos el cursor
    instruccion = f"SELECT * FROM productos WHERE cantidad < 5" # Seleccionamos los productos con stock menor a 5
    cursor.execute(instruccion)
    productos = cursor.fetchall()
    conn.close()

    if productos:
        print(colorama.Fore.RED + "Productos con stock bajo:")
        print("-" * 50)
        for producto in productos:
            id, nombre, descripcion, precio, cantidad, categoria = producto
            print(f"ID: {id}")
            print(f"Nombre: {nombre}")
            print(f"Descripción: {descripcion}")
            print(f"Precio: ${precio:.2f}")
            print(colorama.Fore.YELLOW + f"Cantidad: {cantidad}")
            print(colorama.Fore.RED + f"Categoría: {categoria}")
            print("-" * 50)
    else:
        print(colorama.Fore.GREEN + "No hay productos con stock bajo.")
        print(colorama.Fore.RESET)

#VARIABLES
#CODIGO PRINCIPAL

colorama.init() # Inicializamos colorama
print(colorama.Fore.GREEN + "¡Bienvenido al sistema de inventario!")

while True: # Ciclo infinito para mostrar el menú principal una y otra vez, hasta que el usuario decida salir

    # Menú principal
    print(colorama.Fore.CYAN)
    print("--------------------")
    print("-- MENU PRINCIPAL --")
    print("--------------------")
    print()
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Actualizar cantidad de producto")
    print("4. Eliminar producto")
    print("5. Buscar producto")
    print("6. Reporte de stock bajo")
    print("7. Salir")
    print(colorama.Fore.RESET)
    opcion = int(input(colorama.Fore.RED + "Seleccione una opción: "))
    print(colorama.Fore.RESET)

    if opcion == 1:
        agregarProducto()

    elif opcion == 2:
        leerInventario()

    elif opcion == 3:
        editarCantidad()

    elif opcion == 4:
        eliminarProducto()

    elif opcion == 5:
        identificarProducto()

    elif opcion == 6:
        reporteStockBajo()

    elif opcion == 7:
        print(colorama.Fore.GREEN + "¡Gracias por usar el sistema de inventario!")
        print(colorama.Fore.RESET)
        break
    else:
        print(colorama.Fore.RED + "Opción inválida. Intente de nuevo.")
        print(colorama.Fore.RESET)



