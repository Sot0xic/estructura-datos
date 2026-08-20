class DesbordamientoArray(Exception):
    """Excepción para indicar que el array está lleno."""


class ArrayEstatico:
    """Implementa un array de capacidad fija."""

    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.datos = [None] * capacidad
        self.tamanio = 0

    def insertar(self, elemento):
        """Inserta un elemento al final del array."""
        if self.tamanio >= self.capacidad:
            raise DesbordamientoArray("El array está lleno.")

        self.datos[self.tamanio] = elemento
        self.tamanio += 1

    def obtener(self, indice):
        """Obtiene un elemento mediante su índice."""
        if indice < 0 or indice >= self.tamanio:
            raise IndexError("Índice fuera de rango.")

        return self.datos[indice]

    def eliminar(self, indice):
        """Elimina un elemento y desplaza los elementos posteriores."""
        if indice < 0 or indice >= self.tamanio:
            raise IndexError("Índice fuera de rango.")

        elemento = self.datos[indice]

        for i in range(indice, self.tamanio - 1):
            self.datos[i] = self.datos[i + 1]

        self.datos[self.tamanio - 1] = None
        self.tamanio -= 1

        return elemento

    def __str__(self):
        """Devuelve los elementos almacenados."""
        return str(self.datos[:self.tamanio])


class Nodo:
    """Nodo de una lista enlazada."""

    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class ListaDinamica:
    """Implementa una lista enlazada simple."""

    def __init__(self):
        self.inicio = None
        self.final = None
        self.tamanio = 0

    def insertar_inicio(self, elemento):
        """Inserta un elemento al inicio."""
        nuevo_nodo = Nodo(elemento)
        nuevo_nodo.siguiente = self.inicio
        self.inicio = nuevo_nodo

        if self.final is None:
            self.final = nuevo_nodo

        self.tamanio += 1

    def insertar_final(self, elemento):
        """Inserta un elemento al final."""
        nuevo_nodo = Nodo(elemento)

        if self.final is None:
            self.inicio = nuevo_nodo
            self.final = nuevo_nodo
        else:
            self.final.siguiente = nuevo_nodo
            self.final = nuevo_nodo

        self.tamanio += 1

    def obtener(self, indice):
        """Obtiene un elemento mediante su índice."""
        if indice < 0 or indice >= self.tamanio:
            raise IndexError("Índice fuera de rango.")

        actual = self.inicio

        for _ in range(indice):
            actual = actual.siguiente

        return actual.dato

    def eliminar(self, indice):
        """Elimina un elemento mediante su índice."""
        if indice < 0 or indice >= self.tamanio:
            raise IndexError("Índice fuera de rango.")

        if indice == 0:
            elemento = self.inicio.dato
            self.inicio = self.inicio.siguiente
            self.tamanio -= 1

            if self.tamanio == 0:
                self.final = None

            return elemento

        anterior = self.inicio

        for _ in range(indice - 1):
            anterior = anterior.siguiente

        nodo_eliminado = anterior.siguiente
        anterior.siguiente = nodo_eliminado.siguiente

        if nodo_eliminado == self.final:
            self.final = anterior

        self.tamanio -= 1

        return nodo_eliminado.dato

    def __str__(self):
        """Devuelve los elementos de la lista."""
        elementos = []
        actual = self.inicio

        while actual is not None:
            elementos.append(actual.dato)
            actual = actual.siguiente

        return str(elementos)


def main():
    """Prueba las estructuras."""

    print("=== ARRAY ESTÁTICO ===")

    array = ArrayEstatico(3)

    array.insertar(10)
    array.insertar(20)
    array.insertar(30)

    print("Array:", array)
    print("Elemento en índice 1:", array.obtener(1))

    array.eliminar(1)
    print("Después de eliminar índice 1:", array)

    try:
        array.insertar(40)
        array.insertar(50)
        array.insertar(60)
        array.insertar(70)
    except DesbordamientoArray as error:
        print("Error:", error)

    print("\n=== LISTA DINÁMICA ===")

    lista = ListaDinamica()

    lista.insertar_inicio(20)
    lista.insertar_inicio(10)
    lista.insertar_final(30)
    lista.insertar_final(40)

    print("Lista:", lista)
    print("Elemento en índice 2:", lista.obtener(2))

    lista.eliminar(1)
    print("Después de eliminar índice 1:", lista)


if __name__ == "__main__":
    main()