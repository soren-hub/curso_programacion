
"""
Divide y conquistarás
Nicolás Maquiavelo ??
Julio Cesar ??
"""


class Automovil:
    """
    Clase que representa un automóvil
    """

    def __init__(self, modelo: int, marca: str, color: str):
        self.modelo = modelo
        self.marca = marca
        self.color = color
        self._estado = 'reposo'
        self._motor = Motor(cilindros=4)

    def acelerar(self, tipo: str = 'despacio'):
        """ 
        Este método permite acelerar el automóvil        

        Args:
            tipo (str): Acción . Defaults to 'despacio'.
        """
        if tipo == 'rapida':
            self._motor.inyecta_gasolina(10)
            self._motor.temperaturas(260)
        elif tipo == "frena":
            self._motor.bolsas("activar")
            self._motor.temperaturas(90)
        else:
            self._motor.inyecta_gasolina(3)
            self._motor.temperaturas(130)

        self._estado = 'en_movimiento'


class Motor:
    """
    Clase que representa un motor de un automóvil  
    """

    def __init__(self, cilindros: int, tipo: str = 'gasolina') -> None:
        self.cilindros = cilindros
        self.tipo = tipo
        self._temperatura = 0
        self.litros = 550

    def inyecta_gasolina(self, cantidad: int) -> None:
        """
        Esta función permite inyectar gasolina al motor
        
        Args:
            cantidad (int): cantidad de gasolina a inyectar
        """
        self.litros -= cantidad

    def temperaturas(self, grados: float) -> float:
        """ 
        Esta función permite regular la temperatura del motor
         
        Args:
            grados (float): grados de temperatura 
        """
        if grados > 250:
            self.ventidaores("on")
        else:
            self.ventidaores("off")

        print(f'La temperatura actual es: {grados}°')

    def ventidaores(self, estado: str) -> None:
        """Esta función permite activar los ventiladores
         
        Args: 
            estado (str): estado de los ventiladores
        """
        if estado == "on":
            print('Se ha prendido el ventilador para regular la temperatura')
        else:
            print('Temperatura estable: no requiere de ventilación')

    def bolsas(self, estado: str):
        """Esta función permite activar las bolsas de aire

        Args:
            estado (str): estado de las bolsas de aire
        """
        if estado == "activar":
            print("ACTIVANDO AIRBG")


if __name__ == '__main__':
    auto = Automovil("RS5", "Audi", "Plata")
    auto.acelerar("rapida")
    auto.acelerar("frena")
