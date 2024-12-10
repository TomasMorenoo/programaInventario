import sqlite3 as sql # Importamos la librería sqlite3

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

def agregarProducto():

    nombre= input("Ingrese el nombre del producto: ")
    descripcion = input("Ingrese la descripción del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    cantidad = int(input("Ingrese la cantidad del producto: "))
    categoria = input("Ingrese la categoría del producto: ")

    print("Agregando producto...")
    conn = sql.connect('inventario.db') # Creamos la conexión a la base de datos
    cursor = conn.cursor() # Creamos el cursor
    instruccion = f"INSERT INTO productos (nombre, descripcion, precio, cantidad, categoria) VALUES (?, ?, ?, ?, ?) "
    cursor.execute(instruccion, (nombre, descripcion, precio, cantidad, categoria))
    print(f"Producto '{nombre}' agregado con éxito")
    conn.commit()
    conn.close()

def leerColumna():
    conn = sql.connect('inventario.db') # Creamos la conexión a la base de datos
    cursor = conn.cursor() # Creamos el cursor
    instruccion = f"SELECT * FROM productos"
    cursor.execute(instruccion)
    datos = cursor.fetchall()
    conn.commit()
    conn.close()
    print(datos)

def agregarProductos(listaProductos):
    print("Agregando producto...")
    conn = sql.connect('inventario.db') # Creamos la conexión a la base de datos
    cursor = conn.cursor() # Creamos el cursor
    instruccion = f"INSERT INTO productos VALUES (?, ?, ?, ?, ?, ?)"
    cursor.executemany(instruccion, listaProductos)
    conn.commit()
    conn.close()

def leerOrdenado(field):
    conn = sql.connect('inventario.db') # Creamos la conexión a la base de datos
    cursor = conn.cursor() # Creamos el cursor
    instruccion = f"SELECT * FROM productos ORDER BY {field} DESC" # DEST para ordenar de forma descendente y ASC para ordenar de forma ascendente
    cursor.execute(instruccion)
    datos = cursor.fetchall()
    conn.commit()
    conn.close()
    print(datos)

def buscar():
    conn = sql.connect('inventario.db') # Creamos la conexión a la base de datos
    cursor = conn.cursor() # Creamos el cursor
    parametroBusqueda = input("Ingrese el nombre del producto a buscar: ")
    instruccion = f"SELECT * FROM productos WHERE nombre LIKE '{parametroBusqueda}'" # LIKE para buscar por coincidencias parciales, = para buscar por coincidencias exactas, > para buscar por mayor que, < para buscar por menor que
    cursor.execute(instruccion)
    datos = cursor.fetchall()
    conn.commit()
    conn.close()
    print(datos)

def editarProducto():
    print("Editando producto...")
    conn = sql.connect('inventario.db') # Creamos la conexión a la base de datos
    cursor = conn.cursor() # Creamos el cursor
    instruccion = f"UPDATE productos SET nombre = 'Coca-Cola zero'  WHERE nombre = 'Coca Cola'" 
    cursor.execute(instruccion)
    conn.commit()
    conn.close()

def eliminarProducto():
    print("Eliminando producto...")
    conn = sql.connect('inventario.db') # Creamos la conexión a la base de datos
    cursor = conn.cursor() # Creamos el cursor
    instruccion = f"DELETE FROM productos WHERE nombre = 'Carlos V'" 
    cursor.execute(instruccion)
    conn.commit()
    conn.close()



listaProductos = [
    (2, 'Pepsi', 'Refresco de cola', 15.50, 100, 'Refrescos'),
    (3, 'Sprite', 'Refresco de limón', 15.50, 100, 'Refrescos'),
    (4, 'Fanta', 'Refresco de naranja', 15.50, 100, 'Refrescos'),
    (5, 'Jumex', 'Jugo de manzana', 15.50, 100, 'Jugos'),
    (6, 'Del Valle', 'Jugo de naranja', 15.50, 100, 'Jugos'),
    (7, 'Boing', 'Jugo de guayaba', 15.50, 100, 'Jugos'),
    (8, 'Tang', 'Jugo de naranja', 15.50, 100, 'Jugos'),
    (9, 'Doritos', 'Botana de maíz', 15.50, 100, 'Botanas'),
    (10, 'Cheetos', 'Botana de maíz', 15.50, 100, 'Botanas'),
    (11, 'Ruffles', 'Botana de papa', 15.50, 100, 'Botanas'),
    (12, 'Sabritas', 'Botana de papa', 15.50, 100, 'Botanas'),
    (13, 'Barcel', 'Botana de maíz', 15.50, 100, 'Botanas'),
    (14, 'Gamesa', 'Galletas', 15.50, 100, 'Galletas'),
    (15, 'Marinela', 'Galletas', 15.50, 100, 'Galletas'),
    (16, 'Oreo', 'Galletas', 15.50, 100, 'Galletas'),
    (17, 'Príncipe', 'Galletas', 15.50, 100, 'Galletas'),
    (18, 'Nestlé', 'Chocolate', 15.50, 100, 'Chocolate'),
    (19, 'Carlos V', 'Chocolate', 15.50, 100, 'Chocolate'),
    (20, 'Hershey´s', 'Chocolate', 15.50, 100, 'Chocolate')]


if __name__ == "__main__":
    #createDB()
    #createTable()
    agregarProducto()
    #leerColumna()
    #AgregarProductos(listaProductos)
    #leerOrdenado("nombre")
    #buscar()
    #editarProducto()
    #eliminarProducto()
    

#CODIGO VIEJO

"""
# Lista para almacenar los productos
productos = []

# Función para agregar un producto
def agregar_producto():
        return True  

# Función para ver los productos
def ver_productos():
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
"""