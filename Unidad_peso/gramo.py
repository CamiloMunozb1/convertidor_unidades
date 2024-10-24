
# OPERACIONES DE CONVERSION (GRAMO).

def operacion_miligramo(valor):
    return valor * 1000

def operacion_kilogramo(valor):
    return valor / 1000

def operacion_onza(valor):
    return valor / 28.3495

def operacion_libra(valor):
    return valor / 453.592

# FUNCION PARA USARLA EN EL INDEX DE UNIDAD_PESO.

def gramo():

    # MENU DE OPCIONES PARA CONVERSION.

    print("""
            Elige la operacion a realizar:
            1.Miligramo.
            2.Kilogramo.
            3.Onza.
            4.Libra.
        """)
    try:

        # OPCION PARA ELEGIR LA OPRACION A REALIZAR.

        usuario = int(input("Ingresa de que medida va ser la conversion: "))

        # INGRESO DEL VALOR DE MEDIDA EN GRAMO.

        calculo_valor = float(input("Ingresa el valor en gramos: "))

        # OPCIONES DE USUARIO DONDE LA ELECCION USA LA FUNCION DE CONVERSION Y SE LE PASA EL VALOR DEL USUARIO.

        if usuario == 1:
            print(f"El valor de gramos en miligramos es: {operacion_miligramo(calculo_valor)}")
        elif usuario == 2:
            print(f"El valor de gramos en kilogramos es: {operacion_kilogramo(calculo_valor)}")
        elif usuario == 3:
            print(f"El valor de gramos en onzas es: {operacion_onza(calculo_valor)}")
        elif usuario == 4:
            print(f"El valor de gramos en libras es: {operacion_libra(calculo_valor)}")
    
    # MANEJO DE ERRORES.

    except ValueError:
        print("Error de digitacion, volver a intentar.")
