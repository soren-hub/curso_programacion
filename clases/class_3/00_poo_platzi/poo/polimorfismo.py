
class Persona:

    def __init__(self, nombre):
        self.nombre = nombre

    def avanzar(self):
        print(f'{self.nombre}: Caminando')


class Ciclista(Persona):
    def __init__(self, nombre):
        super().__init__(nombre)

    def avanzar(self):
        print(f'{self.nombre}: Utiliza una bicicleta')


def run():
    persona = Persona('David')
    persona.avanzar()

    ciclista = Ciclista('Edgar')
    ciclista.avanzar()


if __name__ == '__main__':
    run()