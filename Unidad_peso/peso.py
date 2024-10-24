
# FUNCIONES DE CONVERSION QUE SE USARAN EN EL INDEX DE UNIDAD_PESO.

from Unidad_peso.Miligramo import miligramos
from Unidad_peso.gramo import gramo
from Unidad_peso.kilogramo import kilogramo
from Unidad_peso.onza import onza
from Unidad_peso.libra import libras


# FUNCION DE IMPORTACION PARA EL INDEX ORIGINAL.

def unidad_peso():

    # MENU DE USUARIOS.

    print(
        """
            ELIGE UNA UNIDAD DE MEDIDA:
            1. Miligramo.
            2. Gramo.
            3. Kilogramo.
            4. Onza.
            5. Libra.
            6. Atras.
        """
    )
    try:

        # ENTRADA DE USAURIO PARA INGREAR LA OPERACION A REALIZAR.

        usuario = int(input("Ingresa la operacion que deseas hacer: "))

        # OPCIONES IMPORTADAS A LAS OPERACIONES.

        if usuario == 1:
            miligramos()
        elif usuario == 2:
            gramo()
        elif usuario == 3:
            kilogramo()
        elif usuario == 4:
            onza()
        elif usuario == 5:
            libras()
        
        # REGRESO AL INDEX PRINCIPAL.

        elif usuario == 6:
            return
    
    # MANEJO DE ERRORES.
    
    except ValueError:
        print("Error de digitacion, volver a intentar.")

