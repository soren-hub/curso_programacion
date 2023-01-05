cantidad = int(input("¿a Cuántos números quieres sacarle el promedio?"))
lista = []
suma = 0
for i in range(0,cantidad):
    num = int(input("Número"))
    lista.append(num)
    suma = suma + lista[i]
print(lista)
print(suma/cantidad)


def int_to_ordinal(i):
    dict_num = {
        1: "primero",
        2: "segundo",
        3: "tercero",
        4: "cuarto",
        5: "quinto",
        6: "sexto",
        7: "séptimo",
        8: "octavo",
        9: "noveno",
        10: "décimo",
    }
    if i in dict_num:
        return dict_num[i]
    if i > 10:
        return str(i) + "º"
