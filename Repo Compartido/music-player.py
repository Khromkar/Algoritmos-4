# Crear un algoritmo que simule un reproductor de música
# Agregar canciones, reproducir, mostrar información de canción a través de un menú

# Crear un algoritmo que simule un reproductor de música
# Agregar canciones, reproducir, mostrar información de canción a través de un menú

class NodoCancion:
    def __init__(self, dato):
        self.dato = dato
        self.anterior = None
        self.siguiente = None


class ListaReproduccion:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.actual = None  # canción que se está reproduciendo

    def esta_vacia(self):
        return self.cabeza is None

    # Agregar canción al final
    def agregar_cancion(self, nombre):
        nueva = NodoCancion(nombre)

        if self.esta_vacia():
            self.cabeza = self.cola = nueva
        else:
            self.cola.siguiente = nueva
            nueva.anterior = self.cola
            self.cola = nueva

        print(f"Canción '{nombre}' agregada.")

    # Reproducir primera canción
    def reproducir(self):
        if self.esta_vacia():
            print("La lista está vacía.")
        else:
            self.actual = self.cabeza
            print(f"Reproduciendo: {self.actual.dato}")

    # Siguiente canción
    def siguiente(self):
        if self.actual and self.actual.siguiente:
            self.actual = self.actual.siguiente
            print(f"Reproduciendo: {self.actual.dato}")
        else:
            print("No hay siguiente canción.")

    # Canción anterior
    def anterior(self):
        if self.actual and self.actual.anterior:
            self.actual = self.actual.anterior
            print(f"Reproduciendo: {self.actual.dato}")
        else:
            print("No hay canción anterior.")

    # Mostrar canción actual
    def mostrar_actual(self):
        if self.actual:
            print(f"Canción actual: {self.actual.dato}")
        else:
            print("No hay canción en reproducción.")

    # Mostrar toda la lista
    def mostrar_lista(self):
        if self.esta_vacia():
            print("La lista está vacía.")
        else:
            aux = self.cabeza
            print("Lista de reproducción:")
            while aux:
                print(f"- {aux.dato}")
                aux = aux.siguiente


# ====================
# MENÚ PRINCIPAL
# ====================

lista = ListaReproduccion()

while True:
    print("\n--- MENÚ REPRODUCTOR ---")
    print("1. Agregar canción")
    print("2. Reproducir")
    print("3. Siguiente canción")
    print("4. Canción anterior")
    print("5. Mostrar canción actual")
    print("6. Mostrar lista completa")
    print("7. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nombre = input("Nombre de la canción: ")
        lista.agregar_cancion(nombre)

    elif opcion == "2":
        lista.reproducir()

    elif opcion == "3":
        lista.siguiente()

    elif opcion == "4":
        lista.anterior()

    elif opcion == "5":
        lista.mostrar_actual()

    elif opcion == "6":
        lista.mostrar_lista()

    elif opcion == "7":
        print("Saliendo del reproductor...")
        break

    else:
        print("Opción inválida.")

