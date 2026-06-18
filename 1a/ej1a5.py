"""
Enunciado:
Desarrolla un sistema de inventario simple para una tienda, utilizando `dataclasses` para modelar los productos y un
diccionario para mantener el inventario.

Funciones a desarrollar:
- `add_product(name: str, category: str, quantity: int, price: float) -> Product`:
    Descripción:
    Añade un nuevo producto al inventario o actualiza la cantidad y el precio de un producto existente en el
    inventario. Retorna el producto añadido o actualizado.
    Parámetros:
        - `name` (str): Nombre del producto.
        - `category` (str): Categoría del producto.
        - `quantity` (int): Cantidad de unidades del producto.
        - `price` (float): Precio por unidad del producto.

- `list_products() -> str`:
    Descripción:
    Genera y retorna una cadena de texto que lista todos los productos en el inventario, mostrando su nombre,
    categoría, cantidad y precio.

- `find_product(name: str, category: str) -> Optional[Product]`:
    Descripción:
    Busca en el inventario un producto por su nombre y categoría. Retorna el producto si se encuentra, o `None` si no
    existe en el inventario.
    Parámetros:
        - `name` (str): Nombre del producto a buscar.
        - `category` (str): Categoría del producto a buscar.

Ejemplo:
    add_product("Apples", "Fruits", 100, 0.50)
    add_product("Pears", "Fruits", 50, 0.70)
    add_product("Apples", "Fruits", 50, 0.55)

Salida esperada:
- Creación y actualización de productos en el inventario mediante una lista detallada de todos los productos, con sus
nombres, categorías, cantidades y precios.

- Buscar productos específicos en el inventario de una tienda mediante `dataclasses`.
"""

from dataclasses import dataclass
from typing import Dict, Tuple, Optional, List


@dataclass
class Product:
    name: str
    category: str
    quantity: int
    price: float


inventory: Dict[Tuple[str, str], Product] = {}


def add_product(name: str, category: str, quantity: int, price: float) -> Product:
    clave = (name, category)
    if clave in inventory:
        # si ya existe actualizamos cantidad y precio
        p = inventory[clave]
        p.quantity = p.quantity + quantity
        p.price = price
    else:
        inventory[clave] = Product(name, category, quantity, price)
    return inventory[clave]


def list_products() -> str:
    lineas = []
    for clave in inventory:
        p = inventory[clave]
        lineas.append(f"{p.name} ({p.category}) - {p.quantity} units at ${p.price} each")
    return "\n".join(lineas)


def find_product(name: str, category: str) -> Optional[Product]:
    clave = (name, category)
    if clave in inventory:
        return inventory[clave]
    return None


# Para probar el código, descomenta las siguientes líneas
# if __name__ == "__main__":
#     add_product("Apples", "Fruits", 100, 0.50)
#     add_product("Pears", "Fruits", 50, 0.70)
#     add_product("Apples", "Fruits", 50, 0.55)

#     print(list_products())
#     found_product = find_product("Apples", "Fruits")
#     if found_product:
#         print(f"Product found: {found_product.name} ({found_product.category}) - {found_product.quantity} units at ${found_product.price} each")
#     else:
#         print("Product not found.")
