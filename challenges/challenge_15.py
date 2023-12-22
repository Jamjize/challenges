# Reto #15
# ¿CUÁNTOS DÍAS?
# Dificultad: DIFÍCIL

# Enunciado: Crea una función que calcule y retorne cuántos días 
# hay entre dos cadenas de texto que representen fechas.
# - Una cadena de texto que representa una fecha tiene el
#   formato "dd/MM/yyyy".
# - La función recibirá dos String y retornará un Int.
# - La diferencia en días será absoluta (no importa el orden
#   de las fechas).
# - Si una de las dos cadenas de texto no representa una fecha
#   correcta se lanzará una excepción.


from datetime import datetime

def how_many_days(date1, date2):

    try:
        date1 = datetime.strptime(date1, "%d/%m/%Y")
        date2 = datetime.strptime(date2, "%d/%m/%Y")
        
        days_counter = abs(date1 - date2)
        return f"La diferencia de dias es: {days_counter.days}"
    except ValueError:
        return "No ingresaste una fecha valida"

print(how_many_days("14/06/1997", "14/06/2023"))
print(how_many_days("pedro", "14/06/2023"))
