# Inventario para TalentoTech

## Descripción

Este es un programa desarrollado en Python para gestionar un sistema de inventario. Permite agregar, actualizar, eliminar y buscar productos en una base de datos SQLite. Además, incluye funcionalidades para generar reportes de productos con stock bajo.

El programa fue creado como parte de un curso de programación en Python en TalentoTech.

---

## Características principales

- **Agregar productos**: Permite registrar productos con detalles como nombre, descripción, precio, cantidad y categoría.
- **Mostrar inventario**: Muestra todos los productos registrados en la base de datos.
- **Actualizar cantidades**: Actualiza el stock disponible de un producto.
- **Eliminar productos**: Elimina productos especificados por ID.
- **Buscar productos**: Busca productos específicos por ID y muestra sus detalles.
- **Reporte de stock bajo**: Lista los productos con una cantidad inferior a 5 unidades.

---

## Requisitos

### Librerías

Asegúrate de tener instaladas las siguientes librerías antes de ejecutar el programa:

- **colorama**: Para estilizar la salida de texto en la consola.
- **sqlite3**: Incluida por defecto en Python para manejar bases de datos SQLite.

Para instalar colorama:

```bash
pip install colorama
```

### Base de datos

La base de datos `inventario.db` y la tabla `productos` se crean automáticamente al ejecutar el programa si no existen previamente.

---

## Estructura del código

### Importaciones

El programa utiliza:

- **colorama**: Para agregar colores a la salida de la consola.
- **sqlite3**: Para manejar la base de datos SQLite.

### Funciones principales

1. **createDB()**: Crea la base de datos `inventario.db` si no existe.
2. **createTable()**: Crea la tabla `productos` con los campos necesarios.
3. **agregarProducto()**: Agrega un producto al inventario.
4. **leerInventario()**: Muestra el inventario actual.
5. **identificarProducto()**: Busca un producto por ID.
6. **editarCantidad()**: Actualiza la cantidad de un producto.
7. **eliminarProducto()**: Elimina un producto del inventario.
8. **reporteStockBajo()**: Genera un reporte de productos con stock bajo.

### Código principal

El programa presenta un menú interactivo que permite al usuario elegir entre diferentes opciones.

---

## Instrucciones de uso

1. Ejecuta el archivo principal del programa.
2. Selecciona una opción del menú:
   - **1**: Agregar producto.
   - **2**: Mostrar productos.
   - **3**: Actualizar cantidad de producto.
   - **4**: Eliminar producto.
   - **5**: Buscar producto por ID.
   - **6**: Generar reporte de stock bajo.
   - **7**: Salir del programa.
3. Sigue las instrucciones en la consola para cada operación.

---

## Ejemplo de uso

- Agregar un producto:

  ```
  Ingrese el nombre del producto: Laptop
  Ingrese la descripción del producto: Portátil de alto rendimiento
  Ingrese el precio del producto: 1200.50
  Ingrese la cantidad del producto: 10
  Ingrese la categoría del producto: Electrónica
  ```

- Mostrar inventario:

  ```
  ID: 1
  Nombre: Laptop
  Descripción: Portátil de alto rendimiento
  Precio: $1200.50
  Cantidad: 10
  Categoría: Electrónica
  ```

---

## Autor

Este proyecto fue desarrollado por Tomas Moreno Bauer

