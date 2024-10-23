
# FUNCIONES DE CONVERSION QUE SE USARAN EN EL INDEX DE UNIDADES.

from Unidades.milimetro import milimetro
from Unidades.centimetro import centimetro
from Unidades.metro import metro
from Unidades.kilometro import kilometro
from Unidades.pulgada import pulgada
from Unidades. pie import pies
from Unidades.yarda import yardas
from Unidades.milla import millas


# FUNCION DE IMPORTACION PARA EL INDEX ORIGINAL.

def unidad_longitud():

    # MENU DE USUARIOS.

    print(
        """
            ELIGE UNA UNIDAD DE MEDIDA:
                1.milimetro.
                2.centimetro.
                3.metro.
                4.kilometro.
                5.pulgada.  
                6.pie.
                7.yarda.
                8.milla.
                9.Atras
        """
        )
    try:

        # ENTRADA DE USAURIO PARA INGREAR LA OPERACION A REALIZAR.

        usuario = int(input("Ingresa la operacion que deseas hacer: "))

        # OPCIONES IMPORTADAS A LAS OPERACIONES.

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
            yardas()
        elif usuario == 8:
            millas()

        # REGRESO AL INDEX PRINCIPAL.

        elif usuario == 9:
            return
    
    # MANEJO DE ERRORES.
    
    except ValueError:
        print("Error de digitacion, volver a intentar.")