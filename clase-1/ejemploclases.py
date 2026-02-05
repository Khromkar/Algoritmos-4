class Estudiante:
        def __init__(self, documento, nombre, telefono):
            self.documento = documento
            self.nombre = nombre
            self.telefono = telefono


estudiante1 = Estudiante(1036961765,'Steven',3118163757)

print(estudiante1.nombre)