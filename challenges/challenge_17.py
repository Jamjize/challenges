# Reto #17
# LA CARRERA DE OBSTÁCULOS
# Dificultad: MEDIA

# Enunciado: Crea una función que evalúe si un/a atleta ha superado 
# correctamente una carrera de obstáculos.
# - La función recibirá dos parámetros:
#      - Un array que sólo puede contener String con las palabras 
#        "run" o "jump"
#      - Un String que represente la pista y sólo puede contener 
#        "_" (suelo) o "|" (valla)
# - La función imprimirá cómo ha finalizado la carrera:
#      - Si el/a atleta hace "run" en "_" (suelo) y "jump" en 
#        "|" (valla) será correcto y no
#        variará el símbolo de esa parte de la pista.
#      - Si hace "jump" en "_" (suelo), se variará la pista por "x".
#      - Si hace "run" en "|" (valla), se variará la pista por "/".
# - La función retornará un Boolean que indique si ha superado la carrera.
# Para ello tiene que realizar la opción correcta en cada tramo de la pista.

def evaluate_obstacle_course(actions, track):
    index = 0
    expected_action = ''
    modified_track = []

    for obstacle in track:
        if obstacle == '_':
            expected_action = 'run'
        else:
            expected_action = 'jump'

        if actions[index] != expected_action:
            if expected_action == 'jump':
                modified_track.append('/')
            else:
                modified_track.append('x')
        else:
            modified_track.append(obstacle)
        index += 1

    print(modified_track)

    return modified_track == track

athlete_actions = ['run', 'jump', 'run', 'run', 'run', 'run', 'jump', 'jump', 'run']
obstacle_track = '_|__|_|__'
print(evaluate_obstacle_course(athlete_actions, obstacle_track))
