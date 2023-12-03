#  * Reto #3
#  * ¿ES UN NÚMERO PRIMO?
#  * Dificultad: MEDIA
#  *
#  * Enunciado: Escribe un programa que se encargue de comprobar si un número es o no primo.
#  * Hecho esto, imprime los números primos entre 1 y 100.

for num in range(2, 101):
    is_divisible = False
    for divisor in range(2, num):
        if num % divisor == 0:
            is_divisible = True
            break
    
    if is_divisible == False:
        print(num)
        