# Reto #16
# EN MAYÚSCULA
# Dificultad: FÁCIL

# Enunciado: Crea una función que reciba un String de cualquier tipo y se encargue de
# poner en mayúscula la primera letra de cada palabra.
# - No se pueden utilizar operaciones del lenguaje que lo resuelvan directamente.

def make_upper(text):
    splited_text = text.split()
    upper_text = []

    for word in splited_text:
        upper_text.append(word[0].upper() + word[1:])
    
    return " ".join(upper_text)

print(make_upper("hola mundo, aqui estoy"))
