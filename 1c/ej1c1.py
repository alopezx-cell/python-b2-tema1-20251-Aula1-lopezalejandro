"""
Enunciado:
Implementa y compara el rendimiento de dos algoritmos de ordenamiento clásicos con Quicksort y Mergesort, en Python.

Funciones a desarrollar:
- `quicksort(arr: List[int]) -> List[int]`:
    Descripción:
    Ordena una lista de números enteros utilizando el algoritmo Quicksort, dividiendo la lista en subconjuntos menores,
    mayores o iguales a un elemento pivote, y luego ordenando esos subconjuntos recursivamente.
    Parámetros:
        - `arr` (List[int]): Lista de números enteros a ordenar.

- `mergesort(arr: List[int]) -> List[int]`:
    Descripción:
    Ordena una lista de números enteros utilizando el algoritmo Mergesort, dividiendo la lista en mitades hasta obtener
    subconjuntos que se consideran ordenados, para luego mezclar esos subconjuntos de manera ordenada.
    Parámetros:
        - `arr` (List[int]): Lista de números enteros a ordenar.

- `merge(left: List[int], right: List[int]) -> List[int]`:
    Descripción:
    Función auxiliar para el Mergesort que mezcla dos sublistas ordenadas en una sola lista ordenada.
    Parámetros:
        - `left` (List[int]): Sublista izquierda ordenada.
        - `right` (List[int]): Sublista derecha ordenada.

Ejemplo:
    start = time.time()
    sorted_array_quicksort = quicksort(test_array.copy())
    end_time = time.time() - start
    print(f"Quicksort on {size} elements took: {end_time:.5f} seconds.")
    print("First 10 elements after Quicksort:", sorted_array_quicksort[:10])

Salida esperada:
- Demostración del proceso de ordenación de una lista de números enteros con Quicksort y Mergesort, incluyendo la
visualización del tiempo que cada algoritmo toma para ordenar la misma lista.
"""

import random
import time
from typing import List


def quicksort(arr: List[int]) -> List[int]:
    if len(arr) <= 1:
        return arr
    # cogemos el primer elemento como pivote
    pivote = arr[0]
    menores = [x for x in arr[1:] if x < pivote]
    iguales = [x for x in arr if x == pivote]
    mayores = [x for x in arr[1:] if x > pivote]
    return quicksort(menores) + iguales + quicksort(mayores)


def mergesort(arr: List[int]) -> List[int]:
    if len(arr) <= 1:
        return arr
    # dividimos por la mitad
    mid = len(arr) // 2
    izq = mergesort(arr[:mid])
    der = mergesort(arr[mid:])
    return merge(izq, der)


def merge(left: List[int], right: List[int]) -> List[int]:
    res = []
    # copiamos para no modificar los originales
    l = list(left)
    r = list(right)
    while l and r:
        if l[0] < r[0]:
            res.append(l.pop(0))
        else:
            res.append(r.pop(0))
    res.extend(l)
    res.extend(r)
    return res


# Para probar el código, descomenta las siguientes líneas
 # if __name__ == "__main__":
#     sizes = [100]
#     for size in sizes:
#         test_array = [random.randint(1, 100) for _ in range(size)]

#         print(f"\nOriginal array (first 10 elements of {size}):")
#         print(test_array[:10])
#
#         start = time.time()
#         sorted_array_quicksort = quicksort(test_array.copy())
#         end_time = time.time() - start
#         print(f"Quicksort on {size} elements took: {end_time:.5f} seconds.")
##         print("First 10 elements after Quicksort:", sorted_array_quicksort[:10])

#         start = time.time()
#         sorted_array_mergesort = mergesort(test_array.copy())
# #        end_time = time.time() - start
#         print(f"Mergesort on {size} elements took: {end_time:.5f} seconds.")
#         print("First 10 elements after Mergesort:", sorted_array_mergesort[:10])
