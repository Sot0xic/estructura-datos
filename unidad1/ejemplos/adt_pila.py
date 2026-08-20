from abc import ABC, abstractmethod


class ADTPila(ABC):
    """Interfaz abstracta para una estructura de datos tipo pila."""

    @abstractmethod
    def apilar(self, elemento):
        """Agrega un elemento en la cima de la pila."""
        pass

    @abstractmethod
    def desapilar(self):
        """Elimina y devuelve el elemento de la cima."""
        pass

    @abstractmethod
    def cima(self):
        """Devuelve el elemento de la cima sin eliminarlo."""
        pass

    @abstractmethod
    def esta_vacia(self):
        """Indica si la pila está vacía."""
        pass


class PilaArray(ADTPila):
    """Implementación de una pila utilizando una lista de Python."""

    def __init__(self):
        self._elementos = []

    def apilar(self, elemento):
        """Agrega un elemento en la cima de la pila."""
        self._elementos.append(elemento)

    def desapilar(self):
        """Elimina y devuelve el elemento de la cima."""
        if self.esta_vacia():
            raise IndexError("No se puede desapilar una pila vacía.")

        return self._elementos.pop()

    def cima(self):
        """Devuelve el elemento de la cima sin eliminarlo."""
        if self.esta_vacia():
            raise IndexError("La pila está vacía.")

        return self._elementos[-1]

    def esta_vacia(self):
        """Indica si la pila está vacía."""
        return len(self._elementos) == 0


class Nodo:
    """Representa un nodo de una lista enlazada."""

    def __init__(self, elemento, siguiente=None):
        self.elemento = elemento
        self.siguiente = siguiente


class PilaLista(ADTPila):
    """Implementación de una pila utilizando una lista enlazada."""

    def __init__(self):
        self._cima = None

    def apilar(self, elemento):
        """Agrega un elemento en la cima de la pila."""
        nuevo_nodo = Nodo(elemento, self._cima)
        self._cima = nuevo_nodo

    def desapilar(self):
        """Elimina y devuelve el elemento de la cima."""
        if self.esta_vacia():
            raise IndexError("No se puede desapilar una pila vacía.")

        elemento = self._cima.elemento
        self._cima = self._cima.siguiente

        return elemento

    def cima(self):
        """Devuelve el elemento de la cima sin eliminarlo."""
        if self.esta_vacia():
            raise IndexError("La pila está vacía.")

        return self._cima.elemento

    def esta_vacia(self):
        """Indica si la pila está vacía."""
        return self._cima is None


def usar_pila(pila):
    """Demuestra que el cliente funciona con cualquier implementación."""

    pila.apilar(10)
    pila.apilar(20)
    pila.apilar(30)

    print("Cima:", pila.cima())
    print("Desapilado:", pila.desapilar())
    print("Desapilado:", pila.desapilar())
    print("¿Está vacía?:", pila.esta_vacia())


print("=== PilaArray ===")
pila = PilaArray()
usar_pila(pila)

print("\n=== PilaLista ===")
pila = PilaLista()
usar_pila(pila)