# Reto #10
# EXPRESIONES EQUILIBRADAS
# Dificultad: MEDIA

# Enunciado: Crea un programa que comprueba si los paréntesis, llaves y 
# corchetes de una expresión están equilibrados.
# - Equilibrado significa que estos delimitadores se abren y cieran en
#   orden y de forma correcta.
# - Paréntesis, llaves y corchetes son igual de prioritarios. No hay 
#   uno más importante que otro.

# - Expresión balanceada: { [ a( c + d ) ] - 5 }
# - Expresión no balanceada: { a( c + d ) ] - 5 }


expresion1 = '{ [ a( c + d ) ] - 5 }'.replace(" ", "")
expresion2 = '{ a( c + d ) ] - 5 }'.replace(" ", "")

def balanced(expresion):
    char_open = []
    char_dict = {'{':'}', '(':')', '[':']'}

    for caracter in expresion:
        if caracter in char_dict.keys():
            char_open.append(caracter)
        elif caracter in char_dict.values():
            if not char_open or char_dict[char_open.pop()] != caracter:
                return False
    return True


print(balanced(expresion1))
print(balanced(expresion2))