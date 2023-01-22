
"""
Todo en Python es un objeto, incluso los tipos de datos primitivos
Ahora vamos a aprender a crear nuestros propios tipos de datos

Creación de unos tipos de datos personalizados
tenemos la palabra reservada class


Tipos de datos abstractos
Son tipos de datos que nos permiten agrupar datos y funcionalidades
que nos permiten interactuar con esos datos

Formas de interactuar con los datos
- Crear datos 
- Leer datos
- Actualizar datos
- Borrar datos
- Procesar datos

Ventajas de los tipos de datos abstractos

Descomposición del problema
Abstracción
Encapsulamiento
Modularidad
Reutilización
"""

"""
Template de una clase en Python
class NombreClase:
    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2
    
    def metodo(self):
        # Hacer algo
        return 'Soy un método de la clase NombreClase'
        
    def __str__(self):
        return 'Soy un objeto de la clase NombreClase'

objeto = NombreClase(valor1, valor2)
objeto.metodo() -> 'Soy un metodo de la clase NombreClase'
print(objeto) -> 'Soy un objeto de la clase NombreClase'
"""

"""
Las clases solo son plantillas para crear objetos
Existen diferentes tipos de convenciones para las clases
- CamelCase
- Métodos y atributos privados (con guion bajo) -> _atributo
- Métodos y atributos protegidos (con doble guion bajo) -> __atributo
- Métodos y atributos publicos (sin guion bajo) -> atributo

En la practica todo es publico 
"""



class Coordenadas:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distancia(self, otra_coordenada):
        x_diff = (self.x - otra_coordenada.x)**2
        y_diff = (self.y - otra_coordenada.y)**2

        return (x_diff + y_diff)**0.5


if __name__ == '__main__':
    coord_1 = Coordenadas(3, 30)
    coord_2 = Coordenadas(4, 8)

    print(coord_1.distancia(coord_2))
    # Nos permite sdeterminar sí, alguna de las coo es instancia de Coordenadas
    print(isinstance(coord_2, Coordenadas))