"""
Abstracción de objetos.

Nos permite ocultar la complejidad de un objeto y 
mostrar solo la información relevante al usuario.
Lo cual nos da la ventaja de solo interactuar con
los métodos y atributos que nos interesan.
"""

"""   
En este ejemplo, la clase Lavadora tiene métodos
que no son de interés para el usuario, por lo que
se les antepone un guión bajo para indicar que son
privados y no deben ser accedidos por el usuario.
 
Esto se conoce como encapsulación de datos.

A nosotros solo nos interesa el método lavar, 
ya que es el que nos permite interactuar con la
lavadora.

No nos interesa saber como se llena el tanque de
agua, como se añade el jabón, como se lava la ropa
o como se centrifuga la ropa. 
SOLO NOS INTERESA LAVAR LA PUTA ROPA.!!!!!!!!!!!!
"""


class Lavadora:
    def __init__(self):
        pass

    def lavar(self, temperatura='frio'):
        self._llenar_tanque_de_agua(temperatura)
        self._anadir_jabon()
        self._lavar()
        self._centrifugar()

    def _llenar_tanque_de_agua(self, temperatura):
        print(f'Llenando el tanque con agua {temperatura}')

    def _anadir_jabon(self):
        print('Añadiendo jabón')

    def _lavar(self):
        print('Lavando ropa')

    def _centrifugar(self):
        print('Centrifugando la ropa')


if __name__ == '__main__':
    lavadora = Lavadora()
    lavadora.lavar()
