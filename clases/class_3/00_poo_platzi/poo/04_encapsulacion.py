
"""Encapsulacion, getters and setters
 
La encapsulación es un concepto que nos permite 
ocultar la implementación de un objeto,
es decir, que no se pueda (debería) acceder a los atributos
de un objeto desde fuera de la clase.

En python no existe ningun tipo de encapsulacion a nivel de codigo,
pero existen convenciones establecidas para emular este tipo de
comportamiento.

 * Permite agrupar datos y compartamiento en un mismo lugar
 * Controla el acceso a dichos datos
 * Previene modificaciones no autorizadas
 * Protege el codigo
 * Controla la forma en que trabaja el proyecto

*IMPORTANTE* 

Todos esto nace de un concepto de la programacion llamado
defensing programming, que se trata de una programacion defensiva
para controlar el acceso de otras personas a nuestro codigo y la
modificacion del mismo.
""" 
        
class CasillaDeVotacion:
    
    def __init__(self, identificador, pais):
        self._identificador = identificador
        self._pais = pais
        self._region = None

    @property
    def region(self):
        return self._region

    @region.setter
    def region(self, region):
        if region in self._pais:
            self._region = region
        else:
            raise ValueError(f'La region {region} no esta en la lista de países')




if __name__ == '__main__':
    casilla = CasillaDeVotacion(123,['Mexico','Morelos'])
    print(casilla.region)
    casilla.region = 'Mexico'
    print(casilla.region)

