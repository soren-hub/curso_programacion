# args por consola 
import argparse

 
if __name__ == "__main__":
    # Cuando no se dan parametros trae el del dia de ayer
    # cuando se quiere un dia poner la fecha de inicio y fin igual
    parser = argparse.ArgumentParser(description="soy un conjunto de argumentos")

    parser.add_argument(
        "-eleccion_mano",
        action="store",
        dest="eleccion_mano",
        default='tijera',
        help="elija su mano",
    )

    args = parser.parse_args()
    
    mano = args.eleccion_mano

     
    
