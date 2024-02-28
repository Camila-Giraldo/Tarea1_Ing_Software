from Conteo.Archivos import Archivos
from Conteo.Carpetas import Carpetas


carpeta2 = Carpetas('./pruebas2/')
archivo4 = Archivos(carpeta2.getRuta() + 'imagen.jpg')
palabra2 = 'foto'

print(f"La palabra '{palabra2}' aparece {archivo4.contarPalabra(palabra2)} veces")