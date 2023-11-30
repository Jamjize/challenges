
# Reto #7
# CONTANDO PALABRAS
# Dificultad: MEDIA

# Enunciado: Crea un programa que cuente cuantas veces se repite cada palabra 
# y que muestre el recuento final de todas ellas.
# - Los signos de puntuación no forman parte de la palabra.
# - Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
# - No se pueden utilizar funciones propias del lenguaje que lo resuelvan 
# automáticamente.


def word_counter(text):
    """
    Cuenta las veces que se repiten las palabras en un texto dado.

    Args:
    - text (str): Texto al que se le van a contar las palabras

    Returns:
    dict: Un diccionario que tiene como llaves, las palabras repetidas del texto,
          el valor que está asociado a esa clave, es el número de veces, que la palabra
          fue repetida
    """
    text = text.lower().replace(",", "")
    list_words = text.split()
    counter = 0
    dic = {}

    for index in range(len(list_words)):
        actual_word = list_words[index]

        for i in range(len(list_words)):
            if actual_word == list_words[i]:
                counter += 1

        dic[actual_word] = counter
        counter = 0
    
    return dic

print(word_counter("Hello, hello world, world, world, text"))
