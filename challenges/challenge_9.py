# Reto #9
# CÓDIGO MORSE
# Dificultad: MEDIA
#
# Enunciado: Crea un programa que sea capaz de transformar texto natural a código morse
# y viceversa.
# - Debe detectar automáticamente de qué tipo se trata y realizar la conversión.
# - En morse se soporta raya "—", punto ".", un espacio " " entre letras o símbolos y
#   dos espacios entre palabras "  ".
# - El alfabeto morse soportado será el mostrado en 
#   https://es.wikipedia.org/wiki/Código_morse.

morse_dict = {
    'A': '·—', 'B': '—···', 'C': '—·—·', 'CH': '———', 'D': '—··',
    'E': '·', 'F': '··—·', 'G': '——·', 'H': '····', 'I': '··',
    'J': '·———', 'K': '—·—', 'L': '·—··', 'M': '——', 'N': '—·',
    'Ñ': '——·——', 'O': '———', 'P': '·——·', 'Q': '——·—',
    'R': '·—·', 'S': '···', 'T': '—', 'U': '··—', 'V': '···—',
    'W': '·——', 'X': '—··—', 'Y': '—·——', 'Z': '——··',
    '0': '—————', '1': '·————', '2': '··———', '3': '···——',
    '4': '····—', '5': '·····', '6': '—····', '7': '——···',
    '8': '———··', '9': '————·',
    '.': '·—·—·—', ',': '——··——', '?': '··——··',
    '"': '·—··—·', '/': '—··—·', ' ': '  '
}

morse_dict_inverse = {
    '·—': 'A', '—···': 'B', '—·—·': 'C', '———': 'CH', '—··': 'D',
    '·': 'E', '··—·': 'F', '——·': 'G', '····': 'H', '··': 'I',
    '·———': 'J', '—·—': 'K', '·—··': 'L', '——': 'M', '—·': 'N',
    '——·——': 'Ñ', '———': 'O', '·——·': 'P', '——·—': 'Q',
    '·—·': 'R', '···': 'S', '—': 'T', '··—': 'U', '···—': 'V',
    '·——': 'W', '—··—': 'X', '—·——': 'Y', '——··': 'Z',
    '—————': '0', '·————': '1', '··———': '2', '···——': '3',
    '····—': '4', '·····': '5', '—····': '6', '——···': '7',
    '———··': '8', '————·': '9',
    '·—·—·—': '.', '——··——': ',', '··——··': '?',
    '·—··—·': '"', '—··—·': '/', '  ': ' '
}

def translator(text: str):
    morse_text = ""
    normal_text = ""


    if text[0] in morse_dict:
        # Translates normal text to Morse code by iterating through each 
        # character in the input text.
        
        # Builds the Morse code representation of the text.
        for letter in text.upper():
            morse_text += morse_dict[letter] + " "
        return morse_text
    elif text[0] in morse_dict_inverse:
        # Translates Morse code to normal text by splitting the Morse code 
        # into words.

        # Builds the normal text representation based on the Morse
        # code patterns.
        text = text.split("  ")
        for pattern in text:
            normal_text += morse_dict_inverse[pattern]
        return normal_text
    else:
        return "That is not text or Morse code"

print(translator('Hola'))
print(translator('····  ———  ·—··  ·—'))
print(translator('********-'))