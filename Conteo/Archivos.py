import re


class Archivos():

    def __init__(self, ruta: str):
        self.__ruta = ruta

    def getRuta(self) -> str:
        return self.__ruta
    
    def getExtension(self) -> str:
        return self.__ruta.split('.')[-1]
    
    # Verificar que el archivo sea de texto
    def __verificarArchivo(self) -> bool:
        extensiones = ['txt', 'csv', 'json', 'xml']
        if self.getExtension() in extensiones:
            return True
        return False
    
    # Leer el contenido del archivo
    def leerArchivo(self) -> str:
        if self.__verificarArchivo():
            try:
                with open(self.__ruta, 'r') as archivo:
                    return archivo.read()
            except FileNotFoundError:
                return f"El archivo {self.__ruta} no existe"
            except Exception as e:
                return e
        else:
            exit(f"El archivo no es de texto")
            
    
    '''
     Contar la cantidad de veces que aparece una palabra en el archivo
        Parámetros: palabra a buscar
        Retorna: conteo de la palabra en el archivo
    '''
    def contarPalabra(self, palabra: str) -> int:
        contenido = self.leerArchivo()
        # Usar \b para buscar la palabra completa
        apariciones = re.findall(r'\b' + re.escape(palabra) + r'\b', contenido)
        return len(apariciones)
    