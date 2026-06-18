"""
Enunciado:
Desarrolla un conjunto de funciones para la manipulación y transformación de datos textuales a través de operaciones
con bytes y bytearray en Python. Las funciones deberán modificar un texto a bytes, revertir el orden de los bytes,
incrementar el valor de cada byte y finalmente decodificar el resultado a texto.

Las funciones y operaciones a desarrollar son:
- Codificar un texto a bytes: text_to_bytes(text: str) -> bytes, toma una cadena de texto y la codifica en bytes
utilizando UTF-8.
- Revertir el orden de los bytes: reverse_bytes(bytes_data: ByteString) -> bytearray, toma una secuencia de bytes
y devuelve un bytearray con el orden de los bytes invertido.
- Incrementar el valor de cada byte con posible desbordamiento:
increment_bytearray_rollover(byte_array: bytearray) -> bytearray, incrementa en 1 el valor de cada byte, volviendo a
0 si se supera el valor máximo de un byte (255).
- Decodificar bytes a texto: bytes_to_text(bytes_data: Union[bytes, bytearray]) -> str, toma una secuencia de bytes
o bytearray y la decodifica a texto utilizando UTF-8.

Parámetros:
- text (str): Texto original a ser codificado en bytes.
- bytes_data (ByteString): Datos en formato de bytes a ser revertidos.
- byte_array (bytearray): Array de bytes a ser incrementado.

Ejemplo:
    original_text = "Hola Mundo!"
    original_bytes = text_to_bytes(original_text)
    reversed_bytearray = reverse_bytes(original_bytes)
    modified_bytearray = increment_bytearray_rollover(reversed_bytearray)
    processed_text = bytes_to_text(modified_bytearray)

Salida esperada:
- La representación en bytes del texto original, la versión revertida de esta secuencia en formato bytearray, la
versión modificada de este bytearray tras incrementar cada byte, y finalmente, el texto resultante tras decodificar
el bytearray modificado.
"""

from typing import ByteString, Union


def text_to_bytes(text: str) -> bytes:
    # convertimos el texto a bytes con utf-8
    resultado = text.encode("utf-8")
    return resultado


def reverse_bytes(bytes_data: ByteString) -> bytearray:
    # invertimos el orden de los bytes
    arr = bytearray(bytes_data)
    invertido = bytearray()
    i = len(arr) - 1
    while i >= 0:
        invertido.append(arr[i])
        i = i-1
    return invertido


def increment_bytearray_rollover(byte_array: bytearray) -> bytearray:
    resultado = bytearray()
    for b in byte_array:
        nuevo = b + 1
        # si supera 255 volvemos a 0
        if nuevo > 255:
            nuevo = 0
        resultado.append(nuevo)
    return resultado


def bytes_to_text(bytes_data: Union[bytes, bytearray]) -> str:
    return bytes_data.decode("utf-8")


# Para probar el código, descomenta las siguientes líneas
#   if __name__ == "__main__":
#     original_text = "Hola Mundo!"
#     original_bytes = text_to_bytes(original_text)
#     print("Original Bytes:", original_bytes)

#     reversed_bytearray = reverse_bytes(original_bytes)
#     print("Reversed Bytearray:", reversed_bytearray)

#     modified_bytearray = increment_bytearray_rollover(reversed_bytearray)
#     print("Modified Bytearray:", modified_bytearray)

#     processed_text = bytes_to_text(modified_bytearray)
#     print("Processed Text:", processed_text)
