import random


def bubblesort(lista):
    n = len(lista)

    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

    return lista


def run():
    tam = int(input('Tamaño de la lista: '))

    lista = [random.randint(0, 100) for i in range(tam)]
    print(lista)

    lista_ord = bubblesort(lista)

    print(lista_ord)


if __name__ == '__main__':
    run()
