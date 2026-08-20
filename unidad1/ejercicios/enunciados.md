# Ejercicios — Unidad I

## 🎯 Objetivo

Comprender y aplicar los modelos de representación de datos:

- **Abstracto**
- **Estático**
- **Dinámico**
- **Persistente**

---

## 📚 Ejercicios

### 1. ADT de Pila

Diseñar una interfaz abstracta `ADTPila` y crear dos implementaciones:

- `PilaArray`
- `PilaLista`

**Objetivo:** demostrar que el código cliente funciona sin cambios al intercambiar una implementación por la otra.

---

### 2. Estático vs. Dinámico

Implementar las siguientes estructuras:

- `ArrayEstatico(capacidad)` con control de desbordamiento.
- `ListaDinamica` enlazada con inserción al inicio y al final.

Comparar las complejidades de:

| Operación | Comparación |
|---|---|
| Inserción | — |
| Acceso por índice | — |
| Eliminación | — |

---

### 3. Simulación de Datos

Generar **50 registros simulados de estudiantes**, cada uno con:

- Nombre
- Nota
- Grupo

Cargar los datos en ambas estructuras y reportar:

- **Tiempo de inserción**
- **Facilidad de búsqueda**
- **Memoria aproximada**

---

### 4. Persistencia

Guardar y recuperar la estructura de estudiantes utilizando:

- **JSON**
- **Pickle**

Además, explicar en un párrafo **cuándo conviene utilizar cada formato**.

---

## 🚀 Desafío

Implementar una capa de repositorio llamada `RepositorioEstudiantes` con los siguientes métodos:

- `guardar`
- `cargar`
- `agregar`
- `listar`

La implementación debe permitir **cambiar de JSON a Pickle sin modificar el código cliente**.

---

## 📁 Estructura del proyecto

Los ejercicios y ejemplos se organizan de la siguiente manera:

```text
unidad1/
├── ejemplos/
│   ├── adt_pila.py
│   ├── estatico_vs_dinamico.py
│   ├── simulacion_datos.py
│   ├── persistencia/
│   │   ├── persistencia.py
│   │   ├── estudiantes.json
│   │   └── estudiantes.pkl
│   └── repositorio_estudiantes/
│       ├── repositorio_estudiantes.py
│       └── estudiantes.json
│
└── ejercicios/
    └── enunciados.md