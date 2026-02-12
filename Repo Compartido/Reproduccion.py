class Nodo:
    def __init__(self, nombre, duracion):  # Nodo individual por canción
        self.nombre = nombre
        self.duracion = duracion
        self.anterior = None
        self.siguiente = None


class listaDoble:
    def __init__(self):   # Lista doblemente ligada
        self.cabeza = None
        self.cola = None
        self.actual = None

    def vacia(self):  # Revisa si la lista se encuentra vacia
        return self.cabeza == None

    def agregar_cancion(self, nombre, duracion):  # Agrega una cancion a final de la lista
        nuevo = Nodo(nombre, duracion)

        if self.vacia():     # Si la lista esta vacia, el nuevo sera la cabeza
            self.cabeza = nuevo
            self.cola = nuevo
            self.actual = nuevo
        else:  # Se coloca el nuevo nodo al final de la lista
            self.cola.siguiente = nuevo
            nuevo.anterior = self.cola
            self.cola = nuevo

        print("La cancion esta agregada con exito")

    def mostrar_lista(self): # Muestra la lista de los artistas
        temp = self.cabeza

        if temp == None:
            print("La lista de la musica se encuentra vacia")
            return

        print("Lista de canciones:")

        while temp != None: # Recorre la lista desde la cabeza hasta el final
            print("Nombre:", temp.nombre)
            print("Duracion:", temp.duracion, "segundos")
            print("------------")
            temp = temp.siguiente

    def anterior(self):
        actual = self.cabeza
        if self.vacia():
            print("No hay canción en reproducción.")    
            
        else:
            if actual.anterior:
                print(f"Reproduciendo: {actual.anterior.nombre} {actual.anterior.duracion} min")
            else:
                print("No hay una cancion anterior")
                

    def siguiente(self):
        # actual = self.cabeza
        if self.vacia(): 
            print("No hay canción en reproducción.")    
        else: 
            if actual.siguiente:  
                actual = actual.siguiente
                print(f"Reproduciendo: {actual.nombre}")
            else:
                print("No hay una cancion siguiente")


    def duracion_total(self):
        if self.vacia():
            print("No hay ninguna cancion en la lista")
        else:
            print(f"La duracion total es igual a {self.cabeza.duracion} seguntos")
                

# Crear la lista doble
lista = listaDoble()

while True:
    print("======================================================")
    print("=             😹Reproductor de los temas📯           =")
    print("======================================================")
    print("1. Agregar cancion o tema")
    print("2. Duracion total")
    print("3. Lista canciones")
    print("4. Anterior cancion")
    print("5. Siguiente cancion")
    print("6. Salir")

    opcion = input("Seleccione la opcion que mas le llame la atencion: ")

    if opcion == "1":
        nombre = input("Ingrese el nombre de la cancion deseada: ")

        try:  # Evita fallar cuando el usuario ingrese alguna letra
            duracion = int(input("Duracion de la cancion en segundos: "))
            lista.agregar_cancion(nombre, duracion)

        except:
            print("Duración inválida. Debe ingresar un número.")

    elif opcion == "2":
        lista.duracion_total()
        continue

    elif opcion == "3":
        lista.mostrar_lista()
        continue

    elif opcion == "4":
        lista.anterior()
        continue

    elif opcion == "5":
        lista.siguiente()
        continue

    elif opcion == "6":
        print("Saliendo del reproductor...")
        break

    else:
        print("Opción inválida.")