# Factorial Recursivo
def factorial_recursivo(n):
    # Caso base
    if n <= 1:
        print(f"Caso base alcanzado: factorial ({n} = 1)")
        return 1
    
    # Caso recursivo
    return n * factorial_recursivo (n-1) #OJO: Operación matemática después de llamado recursivo

resultado = factorial_recursivo(5)
print(resultado)