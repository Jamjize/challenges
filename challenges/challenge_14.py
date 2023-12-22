# Reto #14
# ¿ES UN NÚMERO DE ARMSTRONG?
# Dificultad: FÁCIL

# Enunciado: Escribe una función que calcule si un número dado es un 
# número de Amstrong (o también llamado narcisista).
# Si no conoces qué es un número de Armstrong, debes buscar 
# información al respecto.

def is_amstrong(num):
    if not isinstance(num, int):
        return "Please enter an integer"
    
    if num <= 0:
        return "Please enter a positive integer"

    exponent = len(str(num))
    result = sum(int(digit) ** exponent for digit in str(num))

    if result == num:
        return True
    else:
        return False

print(is_amstrong(153)) # True
print(is_amstrong(100)) # False
print(is_amstrong("hola")) # msg 1
print(is_amstrong(153.20)) # msg 1
print(is_amstrong(-20)) # msg 2
