
# OPERACIONES DE CONVERSION (KILOMETROS).

def operacion_milimetros(valor):
    return valor * 1_000_000

def operacion_centimetros(valor):
    return valor * 100_000

def operacion_metros(valor):
    return valor * 1000

def operacion_pulgadas(valor):
    return valor * 0.0000254

def operacion_pies(valor):
    return valor * 0.0003048

def operacion_yardas(valor):
    return valor * 0.0009144


# FUNCION PARA USARLA EN EL INDEX DE UNIDAD.

def kilometro():

    # MENU DE OPCIONES PARA CONVERSION.

    print(
        """
            Elige la unidad de medida para realizar la operacion:
            1. Milimetros
            2. Centimetros
            3. Metros
            4. Pulgadas
            5. Pies
            6. Yardas
        """
        )
    try:

        # OPCION PARA ELEGIR LA OPRACION A REALIZAR.

        usuario = int(input("Ingresa la unidad de medida: "))

        # INGRESO DEL VALOR DE MEDIDA EN CENTIMETROS.

        valor_calculo = float(input("Ingresa el valor en kilometros: "))

        # OPCIONES DE USUARIO DONDE LA ELECCION USA LA FUNCION DE CONVERSION Y SE LE PASA EL VALOR DEL USUARIO.

        if usuario == 1:
            print(f"El valor de kilometros en milimetros es: {operacion_milimetros(valor_calculo)}")
        elif usuario == 2:
            print(f"El valor de kilometros en centimetros es: {operacion_centimetros(valor_calculo)}")
        elif usuario == 3:
            print(f"El valor de kilometros en metros es: {operacion_metros(valor_calculo)}")
        elif usuario == 4:
            print(f"El valor de kilometros en pulgadas es: {operacion_pulgadas(valor_calculo)}")
        elif usuario == 5:
            print(f"El valor de kilometros en pies es: {operacion_pies(valor_calculo)}")
        elif usuario == 6:
            print(f"El valor de kilometros en yardas es: {operacion_yardas(valor_calculo)}")

    # MANEJO DE ERRORES
    
    except ValueError:
        print("Error en la digitacion, volver a ingresar un valor valido")