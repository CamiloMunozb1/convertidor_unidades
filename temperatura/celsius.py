
# OPERACIONES DE CONVERSION (CELSIUS).

def calculo_fahrenheit(valor):
    return (valor * 1.8) + 32

def calculo_kelvin(valor):
    return valor + 273.15

# FUNCION PARA USARLA EN EL INDEX DE TEMPERATURA.

def celsius():

    # MENU DE OPCIONES PARA CONVERSION.

    print("""
            Elige la operacion a realizar:
            1. Fahrenheit.
            2. Kelvin.
        """)
    try:

        # OPCION PARA ELEGIR LA OPRACION A REALIZAR.

        usuario = int(input("Ingresa conversion a realizar: "))

        # INGRESO DEL VALOR DE GRADOS EN CELSIUS.

        calculo_valor = float(int("Ingresa el valor en celsius: "))

        # OPCIONES DE USUARIO DONDE LA ELECCION USA LA FUNCION DE CONVERSION Y SE LE PASA EL VALOR DEL USUARIO.

        if usuario == 1:
            print(f"El valor de celsius en Fahrenheit es: {calculo_fahrenheit(calculo_valor)}")
        elif usuario == 2:
            print(f"EL valor de celsius en Kelvin es: {calculo_kelvin(calculo_valor)}")

    # MANEJOR DE ERRORES.
    
    except ValueError:
        print("Error de digitacion, volver a ingresar una entrada valida.")