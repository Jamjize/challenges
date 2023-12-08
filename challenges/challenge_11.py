# Reto #11
# ELIMINANDO CARACTERES
# Dificultad: FÁCIL

# Enunciado: Crea una función que reciba dos cadenas como 
# parámetro (str1, str2) e imprima otras dos cadenas como 
# salida (out1, out2).

# - out1 contendrá todos los caracteres presentes en la str1 pero NO 
#   estén presentes en str2.
# - out2 contendrá todos los caracteres presentes en la str2 pero NO 
#   estén presentes en str1.

def clean_text(str1, str2):
    out1 = str1
    out2 = str2

    for char in str2:
        out1 = out1.replace(char, "")
    
    for char in str1:
        out2 = out2.replace(char, "")
    
    print(out1)
    print(out2)

clean_text("hola", "adios")


#Alternative
# def clean_text(str1, str2):
#     set1 = set(str1)
#     set2 = set(str2)
    
#     out1 = ''.join(set1 - set2)
#     out2 = ''.join(set2 - set1)
    
#     print(out1)
#     print(out2)
    
# clean_text("hola", "adios")
