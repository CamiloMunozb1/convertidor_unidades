
# OPERACIONES DE CONVERSION (ONZAS).

def calculo_miligramo(valor):
    return valor * 28_349_5

def calculo_gramo(valor):
    return valor * 28.3495

def calculo_kilogramo(valor):
    return valor / 35.274

def calculo_libra(valor):
    return valor / 16

# FUNCION PARA USARLA EN EL INDEX DE UNIDAD_PESO

def onza():
    print("""
            Elige la operacion a realizar:
            1. Miligramo.
            2. Gramo.
            3. Kilogramo.
            4. Libra.
        """)
    try:

        # OPCION PARA ELEGIR LA OPRACION A REALIZAR.

        usuario = int(input("Ingresa la operacion que deseas hacer: "))

        # INGRESO DEL VALOR DE MEDIDA EN ONZAS.

        calculo_valor = float(input("Ingresa el valor en onzas: "))

        # OPCIONES DE USUARIO DONDE LA ELECCION USA LA FUNCION DE CONVERSION Y SE LE PASA EL VALOR DEL USUARIO.

        if usuario == 1:
            print(f"El valor de onzas en miligramos es: {calculo_miligramo(calculo_valor)}")
        elif usuario == 2:
            print(f"El valor de onzas en gramos es: {calculo_gramo(calculo_valor)}")
        elif usuario == 3:
            print(f"El valor de onzas en kilogramos es: {calculo_kilogramo(calculo_valor)}")
        elif usuario == 4:
            print(f"El valor de onzas en libras es: {calculo_libra(calculo_valor)}")
    
    # MANEJO DE ERRORES.
    
    except ValueError:
        print("Error de digitacion, volver a intentar.")