
# OPERACIONES DE CONVERSION (KILOGRAMOS).

def calculo_miligramo(valor):
    return valor * 1_000_000

def calculo_gramo(valor):
    return valor * 1000

def calculo_onza(valor):
    return valor * 35.274

def calculo_libra(valor):
    return valor * 2.20462

# FUNCION PARA USARLA EN EL INDEX DE UNIDAD_PESO

def kilogramo():
    print("""
            Elige la operacion a realizar:
            1. Miligramo.
            2. Gramo.
            3. Onza.
            4. Libra.
        """)
    try:

        # OPCION PARA ELEGIR LA OPRACION A REALIZAR.

        usuario = int(input("Ingresa de que medida va ser la conversion: "))

        # INGRESO DEL VALOR DE MEDIDA EN KILOGRAMO.

        valor_calculo = float(input("Ingresa el valor en kilogramos: "))

        # OPCIONES DE USUARIO DONDE LA ELECCION USA LA FUNCION DE CONVERSION Y SE LE PASA EL VALOR DEL USUARIO.

        if usuario == 1:
            print(f"El valor de Kilogramos en milogramos es: {calculo_miligramo(calculo_miligramo)}")
        elif usuario == 2:
            print(f"El valor de kilogramos en gramos es: {calculo_gramo(valor_calculo)}")
        elif usuario == 3:
            print(f"El valor de kilogramos en onzas es: {calculo_onza(valor_calculo)}")
        elif usuario == 4:
            print(f"El valor de kilogramos en libras es: {calculo_libra(valor_calculo)}")
    
    # MANEJO DE ERRORES.

    except ValueError:
        print("Error de digitacion, volver a intentar.")
