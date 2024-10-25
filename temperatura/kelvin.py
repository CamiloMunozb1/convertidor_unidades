
# OPERACIONES DE CONVERSION (KELVIN).

def calculo_celsius(valor):
    return valor - 273.15

def calculo_fahrenheit(valor):
    return (valor - 273.15) * 1.8 + 32

# FUNCION PARA USARLA EN EL INDEX DE TEMPERATURA.

def kelvin():

    # MENU DE OPCIONES PARA CONVERSION.

    print("""
            Elige la operacion a realizar:
            1. Celsius.
            2. Fahrenheit.
        """)
    try:

        # OPCION PARA ELEGIR LA OPRACION A REALIZAR.

        usuario = int(input("Ingresa la conversion que deseas realizar: "))

        # INGRESO DEL VALOR DE GRADOS EN KELVIN.

        calculo_valor = float(input("Ingresa el valor en Kelvin: "))

        # OPCIONES DE USUARIO DONDE LA ELECCION USA LA FUNCION DE CONVERSION Y SE LE PASA EL VALOR DEL USUARIO.

        if usuario == 1:
            print(f"El valor de Kelvin en Celsius es: {calculo_celsius(calculo_valor)}")
        elif usuario == 2:
            print(f"El valor de Kelvin en Fahrenheit es: {calculo_fahrenheit(calculo_valor)}")

    # MANEJO DE ERRORES.
    
    except ValueError:
        print("Error de digitacion, volver a ingresar una entrada valida.")