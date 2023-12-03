# Reto #1
#  * ¿ES UN ANAGRAMA?
#  *
#  * Enunciado: Escribe una función que reciba dos palabras (String) y retorne verdadero o 
#    falso (Boolean) según sean o no anagramas.
#  * Un Anagrama consiste en formar una palabra reordenando TODAS las letras de otra palabra 
#    inicial.
#  * NO hace falta comprobar que ambas palabras existan.
#  * Dos palabras exactamente iguales no son anagrama.

def is_anagram(word1, word2):
    length1 = len(word1)
    length2 = len(word2)
    word1 = word1.lower()
    word2 = word1.lower()
    exist = False

    if word1 == word2:
        return False
    else:
        if length1 == length2:
            for letter in word1:
                if letter in word2:
                    exist = True
                else:
                    return False
        else:
            return False
        
        if exist == True:
            return True

print(is_anagram("amor", "roMa"))