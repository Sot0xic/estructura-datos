import json
import pickle


class RepositorioEstudiantes:
    def __init__(self, archivo, formato="json"):
        self.archivo = archivo
        self.formato = formato

    def guardar(self, estudiantes):
        if self.formato == "json":
            with open(self.archivo, "w", encoding="utf-8") as archivo:
                json.dump(estudiantes, archivo, ensure_ascii=False, indent=4)

        elif self.formato == "pickle":
            with open(self.archivo, "wb") as archivo:
                pickle.dump(estudiantes, archivo)

    def cargar(self):
        if self.formato == "json":
            with open(self.archivo, "r", encoding="utf-8") as archivo:
                return json.load(archivo)

        elif self.formato == "pickle":
            with open(self.archivo, "rb") as archivo:
                return pickle.load(archivo)

    def agregar(self, estudiante):
        estudiantes = self.cargar()
        estudiantes.append(estudiante)
        self.guardar(estudiantes)

    def listar(self):
        return self.cargar()


# Ejemplo usando JSON
repositorio = RepositorioEstudiantes("estudiantes.json", "json")

repositorio.guardar([])

repositorio.agregar({
    "nombre": "Juan",
    "edad": 21,
    "carrera": "Informática"
})

repositorio.agregar({
    "nombre": "Pedro",
    "edad": 22,
    "carrera": "Informática"
})

print("Estudiantes:")
print(repositorio.listar())