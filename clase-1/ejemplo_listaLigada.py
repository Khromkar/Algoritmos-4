class Nodo:
    def __init__(self, nombre, cedula,prioridad):
        self.nombre = nombre
        self.cedula = cedula
        self.prioridad = prioridad
        self.siguiente = None


class Lista:
    def __init__(self):
        self.cabeza = None

    def agregarNodoAlFinal(self,nombre,cedula,prioridad):
        nodo = Nodo(nombre,cedula,prioridad)

        if self.cabeza is None:
            self.cabeza = nodo
            return
        else:
            actual = self.cabeza
            while actual.siguiente is not None: # Nodo va a recorrer la lista hasta que el siguiente nodo sea nulo
                actual = actual.siguiente
            actual.siguiente = nodo
        print("Nodo agregado exitosamente")

    def agregarNodoConPrioridad(self,nombre,cedula,prioridad):
        nodo = Nodo(nombre,cedula,prioridad)

        if self.cabeza is None:
            self.cabeza = nodo
            return
        elif self.cabeza.prioridad > prioridad:
            nodo.siguiente = self.cabeza
            self.cabeza = nodo
        else:
            actual = self.cabeza
            while actual.siguiente and actual.siguiente.prioridad <= prioridad:
                actual = actual.siguiente
            nodo.siguiente = actual.siguiente
            actual.siguiente = nodo

    def imprimirLista(self):
        actual = self.cabeza
        while actual is not None:
            print(f"Nombre: {actual.nombre}, Cedula: {actual.cedula}")
            actual = actual.siguiente

# Instancio lista
lista = Lista()
lista.agregarNodoConPrioridad("Steven",1036961765,3)
lista.agregarNodoConPrioridad("Sara",432678569,1)
lista.agregarNodoAlFinal("Santiago",2349862,2)

lista.imprimirLista()
