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
    conn = sql.connect('inventario.db') # Creamos la conexión a la base de datos
    cursor = conn.cursor() # Creamos el cursor
    instruccion = f"INSERT INTO productos VALUES ('{nombre}', '{descripcion}', {precio}, {cantidad}, '{categoria}')"
    cursor.execute(instruccion)
    conn.commit()
    conn.close()


if __name__ == "__main__":
    #createDB()
    #createTable()
    agregarProducto() 