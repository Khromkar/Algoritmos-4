# Invertir un string
# Hola --> aloH

def invertir(s):
    if len(s) <= 1: # Caso base
        return s
    else:
        return invertir(s[1:]) + s[0] # "Slicing"

#"Hola"
#"ola" "h"
#"la" "o"
#"a" "l"
#   "a"

# Diga si una palabra es palíndromo

# MI INTENTO

def verificar_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    elif (palabra[0]==palabra[len(palabra)-1]):
        return verificar_palindromo(palabra[1:len(palabra)-1])

#print(verificar_palindromo("reconocer"))

# RESPUESTA
def palindromo(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return palindromo(s[1:-1])

# Contar cuantas veces se repite un caracter en un texto

def contar(s, c):
    if len(s) == 0:
        return 0
    cuenta = 1 if s[0] == c else 0
    return cuenta + contar(s[1:],c)
        

class Nodo:
    def __init__(self,dato):
        self.dato = dato
        self.siguiente = None

class Lista:
    def __init__(self):
        self.cabeza = None
    
    def agregar(dato):
        nodo = Nodo(dato)
        if self.cabeza == None:
            self.cabeza = Nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nodo 


# Método que diga la longitud de la lista
    def contar_nodos_recursivos(self, nodo):
        if nodo is None:
            return 0
        return 1 + self.contar_nodos_recursivos(nodo.siguiente) # (!) "Tail recursion?"
    
    def contar_nodos(self):
        return self.contar_nodos_recursivos(self.cabeza)


# Buscar nodo

    def encontrarDato(self,nodo,dato):
        if nodo is None:
            return False
        elif nodo.dato == dato:
            return True
        return self.encontrarDato(nodo.siguiente, dato)

# Tarea (Hacer TODOS LOS MÉTODOS DEL REPRODUCTOR DE MÚSICA RECURSIVOS)