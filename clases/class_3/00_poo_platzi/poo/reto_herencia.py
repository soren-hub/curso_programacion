
class Persona:

    def __init__(self, cantidad, meses):
        self.cantidad = cantidad
        self.meses = meses

    def Salario(self):
        return self.cantidad * self.meses


class Programador(Persona):
    def __init__(self, salario, mes):
        super().__init__(salario, mes)


if __name__ == '__main__':
    pers = Persona(cantidad=12000, meses=5)
    print(pers.Salario())

    pers1 = Programador(salario=30000, mes=4)
    print(pers1.Salario())