#  * Reto #2
#  * LA SUCESIÓN DE FIBONACCI
#  * Dificultad: DIFÍCIL
#  *
#  * Enunciado: Escribe un programa que imprima los 50 primeros números de la sucesión de 
#    Fibonacci empezando en 0.
#  * La serie Fibonacci se compone por una sucesión de números en la que el siguiente siempre
#    es la suma de los dos anteriores.
#  * 0, 1, 1, 2, 3, 5, 8, 13...


new_list = [0, 1]

for i in range(2, 51):
    new_list.append(new_list[i - 1] + new_list[i - 2])

print(new_list)