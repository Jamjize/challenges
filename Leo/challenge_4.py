# Reto #4
# ÁREA DE UN POLÍGONO
# Dificultad: FÁCIL

# Enunciado: Crea UNA ÚNICA FUNCIÓN (importante que sólo sea una) que sea capaz de calcular 
# y retornar el área de un polígono.
# - La función recibirá por parámetro sólo UN polígono a la vez.
# - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
# - Imprime el cálculo del área de un polígono de cada tipo.

def calculate_area(poli: str, base=0.0, altura=0.0, lado=0.0):
    if base < 0 or altura < 0 or lado < 0:
        return "Solo se admiten números positivos."
    
    if poli == "triangulo":
        area = (0.5 * base) * altura
    elif poli == "cuadrado":
        area = lado**2
    elif poli == "rectangulo":
        area = base * altura
    else:
        return "Solo se puede usar: [triangulo, cuadrado, rectangulo]."
    
    return f"El área de un {poli} es: {area}"

print(calculate_area("triangulo", 2, 3))
print(calculate_area("cuadrado", lado=4))
print(calculate_area("rectangulo", 2, 3))
print(calculate_area("rectangulo", 2, -3))