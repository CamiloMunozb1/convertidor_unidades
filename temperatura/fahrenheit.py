
# OPERACIONES DE CONVERSION (FAHRENHEIT).

def calculo_celsius(valor):
    return (valor - 32) * 0.5556

def calculo_kelvin(valor):
    return (valor - 32) * 0.5556 + 273.15

# FUNCION PARA USARLA EN EL INDEX DE TEMPERATURA.

def fahrenheit():

    # MENU DE OPCIONES PARA CONVERSION.

    print("""
            Elige la operacion a realizar:
            1. Celsius.
            2. Kelvin
        """)
    try:

        # OPCION PARA ELEGIR LA OPRACION A REALIZAR.

        usuario = int(input("Ingresa que conversion deseas realizar: "))

        # INGRESO DEL VALOR DE GRADOS EN FAHRENHEIT.

        calculo_valor = float(input("Ingresa el valor en Fahrenheit: "))

        # OPCIONES DE USUARIO DONDE LA ELECCION USA LA FUNCION DE CONVERSION Y SE LE PASA EL VALOR DEL USUARIO.

        if usuario == 1:
            print(f"El valor de Fahrenheit en celsius es: {calculo_celsius(calculo_valor)}")
        elif usuario == 2: 
            print(f"El valor de Fahrenheit en kelvin es: {calculo_kelvin(calculo_valor)}")

    # MANEJO DE ERRORES.
    
    except ValueError:
        print("Error de digitacion, volver a ingresar una entrada valida.")
