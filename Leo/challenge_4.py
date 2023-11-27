# Reto #4
# ÁREA DE UN POLÍGONO
# Dificultad: FÁCIL

# Enunciado: Crea UNA ÚNICA FUNCIÓN (importante que sólo sea una) que sea capaz de calcular 
# y retornar el área de un polígono.
# - La función recibirá por parámetro sólo UN polígono a la vez.
# - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
# - Imprime el cálculo del área de un polígono de cada tipo.

def calculate_area(poli: str, base: float, altura: float, lado=0.0):
    """
    Calcula el área de diferentes polígonos.

    Args:
    - poli (str): El tipo de polígono ("triangulo", "cuadrado" o "rectangulo").
    - base (float): El valor de la base (usado en triángulo y rectángulo).
    - altura (float): El valor de la altura (usado en triángulo y rectángulo).
    - lado (float, opcional): El valor del lado (usado en cuadrado).

    Returns:
    - None: Imprime el área calculada para el polígono especificado.

    """
    if poli == "triangulo":
        area = 0.5 * (base * altura)
    elif poli == "cuadrado":
        area = lado**2
    elif poli == "rectangulo":
        area = base * altura
    else:
        print("Solo se puede usar: [triangulo, cuadrado, rectangulo]")
    
    print(f"El área de un {poli} es: {area}")

# Test con el triángulo
calculate_area("triangulo", 3, 5.13)

# Tests con cuadrado y rectángulo
calculate_area("cuadrado", 4)  # Si no se proporciona el lado, debería imprimir un mensaje de error
calculate_area("rectangulo", 4, 6)

# Ejemplo de uso de un valor no permitido
calculate_area("pentagono", 0, 0)  # Debería imprimir un mensaje de error