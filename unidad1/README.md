# Unidad 1: Modelos de Representación de Datos

## Introducción

Los datos son elementos fundamentales en la programación, ya que permiten representar información que puede ser almacenada, procesada y utilizada por un programa.

En esta unidad se estudian diferentes formas de representar y manejar los datos, considerando su comportamiento, duración y forma de almacenamiento.

---

## 1. ¿Qué es un dato?

Un **dato** es una representación de un valor o hecho que puede ser almacenado y procesado por un sistema.

Algunos ejemplos son:

```python
nombre = "Álvaro"
edad = 21
altura = 1.75
estudiante = True
```

En este caso, `"Álvaro"`, `21`, `1.75` y `True` son datos de diferentes tipos.

Los datos son la base de cualquier programa, ya que permiten almacenar la información necesaria para realizar operaciones y resolver problemas.

---

## 2. Datos abstractos

Los **datos abstractos** permiten representar información mediante una estructura que define qué operaciones se pueden realizar sobre los datos, sin necesidad de conocer todos los detalles internos de su implementación.

Un ejemplo es una **pila (Stack)**, donde se pueden realizar operaciones como:

* Insertar un elemento.
* Eliminar un elemento.
* Consultar el elemento superior.

La abstracción permite centrarse en qué puede hacerse con los datos y no en cómo se implementan internamente.

---

## 3. Datos estáticos

Los **datos estáticos** son aquellos cuya cantidad o tamaño se establece previamente y no cambia durante la ejecución del programa.

Un ejemplo puede ser un arreglo de tamaño fijo:

```python
numeros = [10, 20, 30, 40, 50]
```

En una estructura estática, el espacio destinado a almacenar los datos se determina previamente.

---

## 4. Datos dinámicos

Los **datos dinámicos** pueden cambiar su tamaño o cantidad durante la ejecución del programa.

Por ejemplo, una lista de Python puede crecer o disminuir:

```python
numeros = [10, 20, 30]

numeros.append(40)
numeros.remove(10)
```

Los datos dinámicos son útiles cuando no conocemos de antemano cuántos elementos necesitaremos almacenar.

---

## 5. Datos simulados

Los **datos simulados** son datos generados artificialmente para representar situaciones o comportamientos que podrían ocurrir en un escenario real.

Se utilizan principalmente para realizar pruebas, experimentos y desarrollar programas sin necesidad de utilizar datos reales.

Por ejemplo:

```python
usuarios = [
    {"nombre": "Carlos", "edad": 20},
    {"nombre": "María", "edad": 22},
    {"nombre": "Pedro", "edad": 19}
]
```

Estos datos pueden utilizarse para probar el funcionamiento de un programa.

---

## 6. Datos persistentes

Los **datos persistentes** son aquellos que permanecen almacenados después de que un programa termina su ejecución.

A diferencia de los datos almacenados únicamente en memoria RAM, los datos persistentes pueden recuperarse posteriormente.

Algunos medios utilizados para almacenar datos de forma persistente son:

* Archivos de texto.
* Archivos JSON.
* Bases de datos.
* Archivos CSV.

---

## 7. Persistencia con JSON

**JSON (JavaScript Object Notation)** es un formato utilizado para almacenar e intercambiar datos de forma estructurada.

Su estructura se basa principalmente en pares **clave-valor** y permite representar objetos, listas y diferentes tipos de datos.

Ejemplo de un archivo JSON:

```json
{
    "nombre": "Álvaro",
    "edad": 21,
    "estudiante": true
}
```

En Python podemos utilizar el módulo `json` para trabajar con estos archivos.

### Guardar datos en JSON

```python
import json

usuario = {
    "nombre": "Álvaro",
    "edad": 21
}

with open("usuario.json", "w") as archivo:
    json.dump(usuario, archivo, indent=4)
```

### Leer datos desde JSON

```python
import json

with open("usuario.json", "r") as archivo:
    usuario = json.load(archivo)

print(usuario)
```

De esta manera, los datos pueden guardarse en un archivo y recuperarse posteriormente, permitiendo la **persistencia de la información**.

---

## Conclusión

Los datos pueden representarse y manejarse de diferentes maneras dependiendo de las necesidades de un programa. Los datos abstractos permiten definir operaciones sin preocuparse por su implementación, mientras que los datos estáticos y dinámicos se diferencian principalmente por la posibilidad de modificar su tamaño.

Por otro lado, los datos simulados permiten realizar pruebas utilizando información artificial, y los datos persistentes permiten conservar información después de finalizar la ejecución de un programa. JSON es una herramienta sencilla y ampliamente utilizada para lograr esta persistencia en aplicaciones desarrolladas con Python.
