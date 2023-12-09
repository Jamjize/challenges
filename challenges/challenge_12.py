# Reto #12
# ¿ES UN PALÍNDROMO?
# Dificultad: MEDIA

# Enunciado: Escribe una función que reciba un texto y retorne verdadero o falso (Boolean) según sean o no palíndromos.
# Un Palíndromo es una palabra o expresión que es igual si se lee de izquierda a derecha que de derecha a izquierda.
# NO se tienen en cuenta los espacios, signos de puntuación y tildes.
# Ejemplo: Ana lleva al oso la avellana.

def is_palindrome(text):
    text = text.replace(' ', '')
    text = text.lower() 
    if text == text[::-1]:
        return True
    else:
        return False

print(is_palindrome('Ana lleva al oso la avellana'))
