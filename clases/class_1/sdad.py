import random

while True:

    posibilidades = ["Piedra","Papel", "Tijera"]
    eleccion = input("¿Piedra, Papel o Tijera?")
    dec =  random.choice(posibilidades)


    if eleccion in posibilidades:
        dec =  random.choice(posibilidades)
        print(f'El computador ha escogido {dec}')

        if eleccion == dec:
            print("Por lo tanto es un empate")
        else:

            if eleccion == "Piedra":
                if dec == "Tijera":
                    print("ganaste")
                if dec == "Papel":
                    print("Perdiste")
            if eleccion == "Tijera":
                if dec == "Papel":
                    print("ganaste")
                if dec == "Piedra":
                    print("Perdiste")

            if eleccion == "Tijera":
                if dec == "Papel":
                    print("ganaste")
                if dec == "Piedra":
                    print("Perdiste")

    else: 
        print("DEBES INGRESAR UNA JUGADA VÁLIDA")
