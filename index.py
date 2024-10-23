
# FUNCIONES EN IMPORTACION PARA EL INDEX.

from Unidades.longitud import unidad_longitud
from Unidad_peso.peso import unidad_peso
from temperatura.temperaturas import temperatura


while True:

    # MENU DE USUARIO CON OPCIONES A CADA OPERACION.
    print(
        """
            BIENVENDO AL CONVERTIDOR DE UNIDADES:
            1.LONGITUD
            2.PESO.
            3.TEMPERATURA.
            4.SALIR.
        """
        )
    try:

        # ENTRADA DE USUARIO PARA ELEGIR LA OPERACION.

        usuario = int(input("Que deseas convertir hoy? "))

        #  OPCIONES DE USUARIO CON LAS OPERACIONES IMPORTADAS.

        if usuario == 1:
            unidad_longitud()
        elif usuario == 2:
            unidad_peso()
        elif usuario == 3:
            temperatura()

        # SALIDA DEL PROGRAMA.

        elif usuario == 4:
            print("Muchas gracias por visitar el convertidor.")
            break

    # MANEJO DE ERRORES.
    
    except ValueError:
        print("Error de digitacion, volver a intentar")