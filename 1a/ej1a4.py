"""
Enunciado:
Desarrolla un sistema de gestión de tareas simple en Python, utilizando `Enum` para definir estados de las tareas y
`typing.NamedTuple` para modelar las tareas y tipado estático.

Funciones a desarrollar:
- `create_task(title: str) -> int`:
    Descripción:
    Añade una nueva tarea al sistema con un estado inicial "Pendiente". La función genera un ID único para cada tarea,
    lo asigna junto con el título proporcionado, y retorna el ID de la tarea creada, mantiene la siguiente estructura:
    `tasks[id] = Task(id, title, TaskStatus.PENDING)`.
    Parámetros:
        - `title` (str): El título de la tarea a crear.

- `change_task_status(task_id: int, new_status: TaskStatus) -> bool`:
    Descripción:
    Actualiza el estado de una tarea existente basándose en su ID. Retorna `True` si la operación es exitosa, o `False`
    si la tarea no se encuentra realizada.
    Parámetros:
        - `task_id` (int): El ID de la tarea a actualizar.
        - `new_status` (TaskStatus): El nuevo estado asignado a la tarea.

- `list_tasks() -> None`:
    Descripción:
    Imprime una lista de todas las tareas registradas, manteniendo el siguiente formato: "ID: {task.id},
    Title: {task.title}, Status: {task.status.value}".


Clases y Enums:
- `TaskStatus(Enum)`: Define los posibles estados de una tarea, incluyendo "Pendiente", "En Progreso" y "Completada".
- `Task(typing.NamedTuple)`: Modelo de una tarea, incluyendo campos para ID, título y estado.

Ejemplo:
    id1 = create_task("Learn Python")
    id2 = create_task("Read Enum documentation")
    change_task_status(id1, TaskStatus.IN_PROGRESS)
    change_task_status(id2, TaskStatus.COMPLETED)
    list_tasks()

Salida esperada:
- Creación y actualización exitosa de tareas en el sistema, seguida por una impresión de todas las tareas, mediante
`Enum` para estados de tarea y `typing.NamedTuple` para la estructura de datos de tarea.
"""

from enum import Enum
from typing import NamedTuple, Dict


class TaskStatus(Enum):
    PENDING = "Pending"
    IN_PROGRESS = "In Progress"
    COMPLETED = "Completed"


class Task(NamedTuple):
    id: int
    title: str
    status: TaskStatus


tasks: Dict[int, Task] = {}


def create_task(title: str) -> int:
    # el id es el siguiente numero disponible
    nuevo_id = len(tasks) + 1
    tasks[nuevo_id] = Task(nuevo_id, title, TaskStatus.PENDING)
    return nuevo_id


def change_task_status(task_id: int, new_status: TaskStatus) -> bool:
    if task_id not in tasks:
        return False
    tarea_vieja = tasks[task_id]
    # NamedTuple es inmutable, hay que crear una nueva
    tasks[task_id] = Task(tarea_vieja.id, tarea_vieja.title, new_status)
    return True


def list_tasks() -> None:
    for task_id in tasks:
        t = tasks[task_id]
        print(f"ID: {t.id}, Title: {t.title}, Status: {t.status.value}")


# Para probar el código, descomenta las siguientes líneas
 # if __name__ == "__main__":
#     id1 = create_task("Learn Python")
#     id2 = create_task("Read Enum documentation")
 #     change_task_status(id1, TaskStatus.IN_PROGRESS)
#     change_task_status(id2, TaskStatus.COMPLETED)
#     list_tasks()
