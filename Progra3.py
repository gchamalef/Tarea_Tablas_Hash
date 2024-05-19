import re

class TablaHash:
    def __init__(self, tamano):
        self.tamano = tamano
        self.tabla = [("", (-1, -1))] * tamano

    def funcion_hash(self, x, y):
        return (x * 31 + y) % self.tamano

    def insertar(self, token, x, y):
        indice = self.funcion_hash(x, y)
        while self.tabla[indice][0] != "" and self.tabla[indice][0] != token:
            indice = (indice + 1) % self.tamano
        self.tabla[indice] = (token, (x, y))

    def mostrar(self):
        for token, (x, y) in self.tabla:
            if token != "":
                print(f'Token: "{token}" en ({x}, {y})')

def procesar_texto(texto):
    lineas = texto.split('\n')
    tabla_hash = TablaHash(50)  # Tamaño de la tabla hash

    for numero_de_linea, linea in enumerate(lineas):
        tokens = re.findall(r'\w+|[^\s\w]+', linea)
        indice_de_caracter = 0

        for token in tokens:
            numero_de_columna = linea.find(token, indice_de_caracter)
            tabla_hash.insertar(token, numero_de_linea, numero_de_columna)
            indice_de_caracter = numero_de_columna + len(token)

    tabla_hash.mostrar()

if __name__ == "__main__":
    texto = """int suma = 0;
suma = 54 + 20;"""
    procesar_texto(texto)
