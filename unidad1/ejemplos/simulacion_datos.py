import random
import sys
import time


class DesbordamientoArray(Exception):
    """Excepción cuando el array alcanza su capacidad máxima."""


class ArrayEstatico:
    """Array de capacidad fija."""

    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.datos = [None] * capacidad
        self.tamanio = 0

    def insertar(self, elemento):
        """Inserta un elemento al final."""
        if self.tamanio >= self.capacidad:
            raise DesbordamientoArray("El array está lleno.")

        self.datos[self.tamanio] = elemento
        self.tamanio += 1

    def buscar(self, nombre):
        """Busca un estudiante por nombre."""
        for i in range(self.tamanio):
            if self.datos[i]["nombre"] == nombre:
                return self.datos[i]

        return None


class Nodo:
    """Nodo de una lista enlazada."""

    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class ListaDinamica:
    """Lista enlazada simple."""

    def __init__(self):
        self.inicio = None
        self.final = None
        self.tamanio = 0

    def insertar_final(self, elemento):
        """Inserta un elemento al final."""
        nuevo_nodo = Nodo(elemento)

        if self.inicio is None:
            self.inicio = nuevo_nodo
            self.final = nuevo_nodo
        else:
            self.final.siguiente = nuevo_nodo
            self.final = nuevo_nodo

        self.tamanio += 1

    def buscar(self, nombre):
        """Busca un estudiante por nombre."""
        actual = self.inicio

        while actual is not None:
            if actual.dato["nombre"] == nombre:
                return actual.dato

            actual = actual.siguiente

        return None


def generar_estudiantes(cantidad):
    """Genera registros simulados de estudiantes."""
    nombres = [
        "Ana", "Carlos", "Maria", "Luis", "Pedro",
        "Sofia", "Diego", "Laura", "Juan", "Valeria",
    ]

    estudiantes = []

    for i in range(cantidad):
        estudiante = {
            "nombre": f"{random.choice(nombres)}_{i + 1}",
            "nota": round(random.uniform(0, 100), 2),
            "grupo": random.choice(["A", "B", "C"]),
        }

        estudiantes.append(estudiante)

    return estudiantes


def medir_insercion_array(estudiantes):
    """Mide el tiempo de inserción en el array."""
    array = ArrayEstatico(len(estudiantes))

    inicio = time.perf_counter()

    for estudiante in estudiantes:
        array.insertar(estudiante)

    fin = time.perf_counter()

    return array, fin - inicio


def medir_insercion_lista(estudiantes):
    """Mide el tiempo de inserción en la lista."""
    lista = ListaDinamica()

    inicio = time.perf_counter()

    for estudiante in estudiantes:
        lista.insertar_final(estudiante)

    fin = time.perf_counter()

    return lista, fin - inicio


def estimar_memoria_array(array):
    """Estima la memoria ocupada por el array."""
    memoria = sys.getsizeof(array.datos)

    for estudiante in array.datos[:array.tamanio]:
        memoria += sys.getsizeof(estudiante)

        for clave, valor in estudiante.items():
            memoria += sys.getsizeof(clave)
            memoria += sys.getsizeof(valor)

    return memoria


def estimar_memoria_lista(lista):
    """Estima la memoria ocupada por la lista."""
    memoria = sys.getsizeof(lista)

    actual = lista.inicio

    while actual is not None:
        memoria += sys.getsizeof(actual)
        memoria += sys.getsizeof(actual.dato)

        for clave, valor in actual.dato.items():
            memoria += sys.getsizeof(clave)
            memoria += sys.getsizeof(valor)

        actual = actual.siguiente

    return memoria


def main():
    """Ejecuta la simulación."""

    cantidad = 50

    estudiantes = generar_estudiantes(cantidad)

    array, tiempo_array = medir_insercion_array(estudiantes)
    lista, tiempo_lista = medir_insercion_lista(estudiantes)

    estudiante_buscado = estudiantes[25]["nombre"]

    inicio = time.perf_counter()
    resultado_array = array.buscar(estudiante_buscado)
    tiempo_busqueda_array = time.perf_counter() - inicio

    inicio = time.perf_counter()
    resultado_lista = lista.buscar(estudiante_buscado)
    tiempo_busqueda_lista = time.perf_counter() - inicio

    memoria_array = estimar_memoria_array(array)
    memoria_lista = estimar_memoria_lista(lista)

    print("=== SIMULACIÓN DE DATOS ===")
    print(f"Cantidad de estudiantes: {cantidad}")

    print("\n--- TIEMPO DE INSERCIÓN ---")
    print(f"Array estático: {tiempo_array:.10f} segundos")
    print(f"Lista dinámica: {tiempo_lista:.10f} segundos")

    print("\n--- BÚSQUEDA ---")
    print(f"Estudiante buscado: {estudiante_buscado}")
    print(f"Array estático: {resultado_array}")
    print(f"Lista dinámica: {resultado_lista}")

    print("\nTiempo de búsqueda:")
    print(
        f"Array estático: "
        f"{tiempo_busqueda_array:.10f} segundos"
    )
    print(
        f"Lista dinámica: "
        f"{tiempo_busqueda_lista:.10f} segundos"
    )

    print("\n--- MEMORIA APROXIMADA ---")
    print(f"Array estático: {memoria_array} bytes")
    print(f"Lista dinámica: {memoria_lista} bytes")


if __name__ == "__main__":
    main()