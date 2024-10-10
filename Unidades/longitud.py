from Unidades.milimetro import milimetro
from Unidades.centimetro import centimetro
from Unidades.metro import metro

def unidad_longitud():
    print("""
        ELIGE UNA UNIDAD DE MEDIDA:
            1.milimetro.
            2.centimetro.
            3.metro.
            4.kilometro.
            6.pulgada.  
            7.pie.
            8.yarda
            9.milla
            """
            )
    try:
        usuario = int(input("Ingresa la operacion que deseas hacer: "))
        if usuario == 1:
            milimetro()
        elif usuario == 2:
            centimetro()
        elif usuario == 3:
            metro()
    except ValueError:
        print("Error de digitacion, volver a intentar")