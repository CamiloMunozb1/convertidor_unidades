from Unidad_peso.Miligramo import miligramos
from Unidad_peso.gramo import gramo
from Unidad_peso.kilogramo import kilogramo



def unidad_peso():
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
        usuario = int(input("Ingresa la operacion que deseas hacer: "))
        if usuario == 1:
            miligramos()
        elif usuario == 2:
            gramo()
        elif usuario == 3:
            kilogramo()
        elif usuario == 4:
            print("Proxima funcion")
        elif usuario == 5:
            print("Proxima funcion")
        elif usuario == 6:
            return
    except ValueError:
        print("Error de digitacion, volver a intentar.")

