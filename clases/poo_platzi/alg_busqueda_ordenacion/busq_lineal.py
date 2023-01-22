import random


def busq_lineal(lista, objetivo):
    match = False

    for i in lista:
        # O(n)
        if i == objetivo:
            match = True
            break
    return match


def run():
    tam = int(input('Tamaño de la lista: '))
    obj = int(input('Objetivo: '))

    lista = [random.randint(0, 100) for i in range(tam)]
    find = busq_lineal(lista, obj)
    print(lista)
    print(f'El elemento {obj} {"esta" if find else "no esta"}')


if __name__ == '__main__':
    run()