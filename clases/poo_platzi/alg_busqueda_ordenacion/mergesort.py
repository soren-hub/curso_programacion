import random


def mergesort(lista):
    if len(lista) > 1:
       medio = len(lista) // 2
       izquierda = lista[:medio]
       derecha = lista[medio:]

       # Llamada recursiva en cada mitad
       mergesort(izquierda)
       mergesort(derecha)

       # Iteradores para recorrer las dos sublistas
       # k es el iterador para la lista principal
       i, j, k = 0, 0, 0

       while i < len(izquierda) and j < len(derecha):
           if izquierda[i] < derecha[j]:
               lista[k] = izquierda[i]
               i += 1
           else:
               lista[k] = derecha[j]
               j += 1
           k += 1
       while i < len(izquierda):
            lista[k] = izquierda[i]
            i += 1
            k += 1
       while j < len(derecha):
            lista[k] = derecha[j]
            j += 1
            k += 1

       print(f'Izquierda: {izquierda}, derecha: {derecha}')
       print(lista)
       print('-'*30)

    return lista


def run():
    tam = int(input('Tamaño de la lista: '))

    lista = [random.randint(0, 100) for i in range(tam)]
    print(lista)

    lista_ord = mergesort(lista)

    print(lista_ord)


if __name__ == '__main__':
    run()
