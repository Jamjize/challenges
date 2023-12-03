# ASPECT RATIO DE UNA IMAGEN
#  Dificultad: DIFÍCIL

#  Enunciado: Crea un programa que se encargue de calcular el aspect ratio de una imagen a 
#  partir de una url.
#  - Url de ejemplo: 
#    https://raw.githubusercontent.com/mouredev/mouredev/master/mouredev_github_profile.png
#  - Por ratio hacemos referencia por ejemplo a los "16:9" de una imagen de 1920*1080px.

import urllib.request
from PIL import Image

url = "https://raw.githubusercontent.com/mouredev/mouredev/master/mouredev_github_profile.png"
image = Image.open(urllib.request.urlopen(url))
width, height = image.size
aspect_ratio = width / height
print(f"El aspect ratio de la imagen es: {aspect_ratio}")