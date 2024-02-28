from Conteo.Archivos import Archivos
import os


class Carpetas():
    def __init__(self, ruta: str):
        self.__ruta = ruta
        self.__archivos = []

    def getRuta(self) -> str:
        return self.__ruta

    def agregarArchivo(self, archivo: Archivos):
        self.__archivos.append(archivo)
    
    # Verificar que la ruta si exista
    def verificarRuta(self) -> bool:
        if os.path.exists(self.__ruta):
            return True
        return False
    
    # Verificar que la ruta de la carpeta si contenga archivos con extensión txt, csv, json y xml
    def verificarArchivos(self) -> bool:
        if self.verificarRuta():
            try:
                extensiones = ['txt', 'csv', 'json', 'xml']
                for archivo in self.__archivos:
                    if archivo.getExtension() not in extensiones:
                        return False
                return True
            except Exception as e:
                return e
        return False

    # Contar la cantidad de veces que aparece una palabra en los archivos de la carpeta
    def contarPalabra(self, palabra: str) -> int:
        if self.verificarArchivos():
            for archivo in self.__archivos:
                conteo += archivo.contarPalabra(palabra)
            return conteo
