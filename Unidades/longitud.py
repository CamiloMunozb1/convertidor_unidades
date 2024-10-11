from Unidades.milimetro import milimetro
from Unidades.centimetro import centimetro
from Unidades.metro import metro
from Unidades.kilometro import kilometro
from Unidades.pulgada import pulgada
from Unidades. pie import pies

def unidad_longitud():
    print("""
        ELIGE UNA UNIDAD DE MEDIDA:
            1.milimetro.
            2.centimetro.
            3.metro.
            4.kilometro.
            5.pulgada.  
            6.pie.
            7.yarda
            8.milla
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
        elif usuario == 4:
            kilometro()
        elif usuario == 5:
            pulgada()
        elif usuario == 6:
            pies()
        elif usuario == 7:
            print("Proxima funcion")
        elif usuario == 8:
            print("Proxima funcion")
    except ValueError:
        print("Error de digitacion, volver a intentar")