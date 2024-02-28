from Conteo.Archivos import Archivos
from Conteo.Carpetas import Carpetas

carpeta1 = Carpetas('./pruebas1/')
archivo1 = Archivos(carpeta1.getRuta() + 'Texto1.txt')
archivo2 = Archivos(carpeta1.getRuta() + 'Texto2.txt')
archivo3 = Archivos(carpeta1.getRuta() + 'Texto3.txt')
carpeta1.agregarArchivo(archivo1)
carpeta1.agregarArchivo(archivo2)
carpeta1.agregarArchivo(archivo3)

palabra1 = 'arar'

print(f"La palabra '{palabra1}' aparece {archivo1.contarPalabra(palabra1)} veces")
print(f"La palabra '{palabra1}' aparece {archivo2.contarPalabra(palabra1)} veces")
print(f"La palabra '{palabra1}' aparece {archivo3.contarPalabra(palabra1)} veces")

print(f"La palabra '{palabra1}' aparece {carpeta1.contarPalabra(palabra1)} veces en los archivos de la carpeta {carpeta1.getRuta()}")