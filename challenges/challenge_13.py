# Reto #13
# FACTORIAL RECURSIVO
# Dificultad: FÁCIL

# Enunciado: Escribe una función que calcule y retorne el factorial de un número dado de forma recursiva.

def factorial(num):
    fact_num = 1
    for i in range(1, num + 1):
        fact_num *= i
    
    return fact_num

print(factorial(5))
