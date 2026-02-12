# Algoritmo recursivo de cuetna regresiva

def cuenta_regresiva(n):
    if n<=0:
        print("Fin")
        return
    print(n)
    cuenta_regresiva(n-1)