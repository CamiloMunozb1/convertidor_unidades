from Unidades.longitud import unidad_longitud

while True:
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
        usuario = int(input("Que deseas convertir hoy? "))
        if usuario == 1:
            unidad_longitud()
        elif usuario == 2:
            print("proxima funcion")
        elif usuario == 3:
            print("proxima funcion")
        elif usuario == 4:
            print("Muchas gracias por visitar el convertidor.")
            break
    except ValueError:
        print("Error de digitacion, volver a intentar")