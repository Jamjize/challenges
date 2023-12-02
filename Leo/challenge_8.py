# Reto #8
# DECIMAL A BINARIO
# Dificultad: FÁCIL
# 
# Enunciado: Crea un programa se encargue de transformar un número decimal a 
# binario sin utilizar funciones propias del lenguaje que lo hagan directamente.

binary = []
decimal = 64

while True:
    binary.append(decimal % 2)
    decimal = decimal // 2

    if decimal == 0:
        break

print(binary[::-1])