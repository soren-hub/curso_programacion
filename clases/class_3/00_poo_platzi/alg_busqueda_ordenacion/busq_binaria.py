import random


def busq_binaria(lista, comienzo, final, objetivo, cont=0):
    cont += 1
    print(f'Buscando {objetivo} entre {lista[comienzo]} y {lista[final - 1]}')

    if comienzo > final:
        return False, cont

    medio = (comienzo + final) // 2

    if lista[medio] == objetivo:        
        return True, cont
    elif lista[medio] < objetivo:
        return busq_binaria(lista, medio+1, final, objetivo,cont=cont)
    else:
        return busq_binaria(lista, comienzo, medio-1, objetivo, cont=cont)


def run():
    tam = int(input('Tamaño de la lista: '))
    obj = int(input('Objetivo: '))

    lista = sorted([random.randint(0, 100) for i in range(tam)])
    (find, cont) = busq_binaria(lista, 0, len(lista), obj)

    print(lista)
    print(f'El elemento {obj} {"esta" if find else "no esta"}')
    print(cont)


if __name__ == '__main__':
    run()