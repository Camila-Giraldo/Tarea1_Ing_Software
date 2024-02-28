from Conteo.Carpetas import Carpetas

carpeta = Carpetas('./incorrecta/')
palabra = 'ejemplo'

print(f"La palabra '{palabra}' aparece {carpeta.contarPalabra(palabra)} veces en los archivos de la carpeta")