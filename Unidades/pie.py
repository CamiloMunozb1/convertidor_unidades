
# OPERACIONES DE CONVERSION (PIES).

def calculo_milimetro(valor):
    return valor / 304.8

def calculo_centimetros(valor):
    return valor / 30.48

def calculo_metros(valor):
    return valor * 3.28084

def calculo_pulgadas(valor):
    return valor / 12

def calculo_yardas(valor):
    return valor * 3

def calculo_kilometros(valor):
    return valor * 3280.84

# FUNCION PARA USARLA EN EL INDEX DE UNIDAD.

def pies():

    # MENU DE OPCIONES PARA CONVERSION.

    print(
        """
            Elige la unidad de medida para realizar la operacion:
            1. Milimetro.
            2. Centimetro.
            3. Metros.
            4. Pulgadas.
            5. Yardas.
            6. Kilometros.
        """
        )
    try:

        # OPCION PARA ELEGIR LA OPRACION A REALIZAR.

        usuario = int(input("Ingresa la unidad de medida: "))

        # INGRESO DEL VALOR DE MEDIDA EN PIES.

        valor_calculo = float(input("Ingresa el valor en pies: "))

        # OPCIONES DE USUARIO DONDE LA ELECCION USA LA FUNCION DE CONVERSION Y SE LE PASA EL VALOR DEL USUARIO.

        if usuario == 1:
            print(f"El valor de pies en milimetros es: {calculo_milimetro(valor_calculo)}")
        elif usuario == 2:
            print(f"El valor de pies en centimetros es: {calculo_centimetros(valor_calculo)}")
        elif usuario == 3:
            print(f"El valor de pies en metros es: {calculo_metros(valor_calculo)}")
        elif usuario == 4:
            print(f"El valor de pies en pulgadas es: {calculo_pulgadas(valor_calculo)}")
        elif usuario == 5:
            print(f"El valor de pies en yardas es {calculo_yardas(valor_calculo)}")
        elif usuario == 6:
            print(f"El valor de pies en kilometros es: {calculo_kilometros(valor_calculo)}")
    
    # MANEJO DE ERROPRES.
    
    except ValueError:
        print("Error en la digitacion, volver a ingresar un valor valido")