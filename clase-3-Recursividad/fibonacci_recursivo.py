# El hecho de que un algoritmo sea pequeño no significa que es eficiente
# Sobretodo si implica recursividad

def fibonacci_simple(n):
    if n <= 1:
        return n
    # Hay dos llamados recursivos seguidos de dos operaciones matemáticas
    # Esto hace que la complejidad de ejecución aumente muy rápidamente según (n)
    return fibonacci_simple(n - 1) + fibonacci_simple(n-2)

print("Resultado")
print(fibonacci_simple(40))