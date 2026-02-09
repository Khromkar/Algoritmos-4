# Crear un algoritmo que simule un reproductor de música
# Agregar canciones, reproducir, mostrar información de canción a través de un menú

class NodoCancion: #Nodo individual por canción
    def __init__(self,dato):
        self.dato = dato
        self.anterior = None
        self.siguiente = None

class ListaReproduccion: #Lista doblemente ligada
    def __init__(self):
        self.cabeza = None
        self.cola = None

    # Revisar si la lista está vacía
    def esta_vacia(self):
        return self.cabeza is None

        