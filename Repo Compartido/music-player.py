# Crear un algoritmo que simule un reproductor de música
# Agregar canciones, reproducir, mostrar información de canción a través de un menú


class NodoCancion:
    def __init__(self, nombre, duracion):
        self.nombre = nombre
        self.duracion = duracion  # duración o tiempo de la canción en minutos
        self.anterior = None
        self.siguiente = None


class ListaReproduccion:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.actual = None

    def esta_vacia(self):
        return self.cabeza is None

    # Agregar canción
    def agregar_cancion(self, nombre, duracion):
        nueva = NodoCancion(nombre, duracion)

        if self.esta_vacia():
            self.cabeza = self.cola = nueva
        else:
            self.cola.siguiente = nueva
            nueva.anterior = self.cola
            self.cola = nueva

        print(f"Canción '{nombre}' agregada ({duracion} min).")

    # Reproducir desde el inicio
    def reproducir(self):
        if self.esta_vacia():
            print("La lista está vacía.")
        else:
            self.actual = self.cabeza
            print(f"Reproduciendo: {self.actual.nombre} "
                  f"({self.actual.duracion} min)")

    # Siguiente canción con repetición al llegar a la ultima 
    def siguiente(self):
        if self.actual:
            if self.actual.siguiente:
                self.actual = self.actual.siguiente
            else:
                self.actual = self.cabeza  # vuelve al inicio

            print(f"Reproduciendo: {self.actual.nombre} "
                  f"({self.actual.duracion} min)")
        else:
            print("No hay canción en reproducción.")

    # Canción anterior
    def anterior(self):
        if self.actual and self.actual.anterior:
            self.actual = self.actual.anterior
            print(f"Reproduciendo: {self.actual.nombre} "
                  f"({self.actual.duracion} min)")
        else:
            print("No hay canción anterior.")

    # Mostrar canción actual
    def mostrar_actual(self):
        if self.actual:
            print(f"Canción actual: {self.actual.nombre} "
                  f"({self.actual.duracion} min)")
        else:
            print("No hay canción en reproducción.")

    # Mostrar lista completa
    def mostrar_lista(self):
        if self.esta_vacia():
            print("La lista está vacía.")
        else:
            aux = self.cabeza
            print("Lista de reproducción:")
            while aux:
                print(f"- {aux.nombre} ({aux.duracion} min)")
                aux = aux.siguiente



# MENÚ 
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
        duracion = float(input("Duración (minutos): "))
        lista.agregar_cancion(nombre, duracion)

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


