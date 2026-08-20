import json
import pickle


def guardar_json(estudiantes, nombre_archivo):
    """Guarda los estudiantes en un archivo JSON."""
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        json.dump(estudiantes, archivo, indent=4, ensure_ascii=False)


def cargar_json(nombre_archivo):
    """Recupera los estudiantes desde un archivo JSON."""
    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        return json.load(archivo)


def guardar_pickle(estudiantes, nombre_archivo):
    """Guarda los estudiantes en un archivo Pickle."""
    with open(nombre_archivo, "wb") as archivo:
        pickle.dump(estudiantes, archivo)


def cargar_pickle(nombre_archivo):
    """Recupera los estudiantes desde un archivo Pickle."""
    with open(nombre_archivo, "rb") as archivo:
        return pickle.load(archivo)


def crear_estudiantes():
    """Crea una lista de estudiantes de ejemplo."""
    return [
        {
            "nombre": "Ana",
            "nota": 85,
            "grupo": "A",
        },
        {
            "nombre": "Carlos",
            "nota": 72,
            "grupo": "B",
        },
        {
            "nombre": "Maria",
            "nota": 91,
            "grupo": "A",
        },
        {
            "nombre": "Luis",
            "nota": 68,
            "grupo": "C",
        },
        {
            "nombre": "Sofia",
            "nota": 95,
            "grupo": "B",
        },
    ]


def main():
    """Ejecuta la demostración de persistencia."""

    estudiantes = crear_estudiantes()

    archivo_json = "estudiantes.json"
    archivo_pickle = "estudiantes.pkl"

    # Guardar
    guardar_json(estudiantes, archivo_json)
    guardar_pickle(estudiantes, archivo_pickle)

    print("Datos guardados correctamente.")

    # Recuperar
    estudiantes_json = cargar_json(archivo_json)
    estudiantes_pickle = cargar_pickle(archivo_pickle)

    print("\n=== DATOS RECUPERADOS DESDE JSON ===")

    for estudiante in estudiantes_json:
        print(estudiante)

    print("\n=== DATOS RECUPERADOS DESDE PICKLE ===")

    for estudiante in estudiantes_pickle:
        print(estudiante)


if __name__ == "__main__":
    main()