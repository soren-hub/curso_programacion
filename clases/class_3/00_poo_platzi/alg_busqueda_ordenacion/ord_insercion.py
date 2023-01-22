import random


def insercion(lista):

    for indice in range(1, len(lista)):
        valor_actual = lista[indice]
        posicion_actual = indice

        while posicion_actual > 0 and lista[posicion_actual -1] > valor_actual:
            lista[posicion_actual] = lista[posicion_actual - 1]
            posicion_actual -= 1

        lista[posicion_actual] = valor_actual

    return lista


def run():
    tam = int(input('Tamaño de la lista: '))

    lista = [random.randint(0, 100) for i in range(tam)]
    print(lista)

    lista_ord = insercion(lista)

    print(lista_ord)


if __name__ == '__main__':
    run()

