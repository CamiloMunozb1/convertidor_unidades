
# FUNCIONES DE CONVERSION QUE SE USARAN EN EL INDEX DE TEMPERATURA.

from temperatura.celsius import celsius
from temperatura.fahrenheit import fahrenheit
from temperatura.kelvin import kelvin

# FUNCION DE IMPORTACION PARA EL INDEX ORIGINAL.

def temperatura():

    # MENU DE USUARIOS.

    print("""
            BIENVENIDO AL CONVERTIDOR DE TEMPERATURAS:
            1. Celsius.
            2. Fahrenheit.
            3. Kelvin.
            4. Atras.
        """)
    try:

        # ENTRADA DE USAURIO PARA INGREAR LA OPERACION A REALIZAR.

        usuario = int(input("Ingresa la operacion que deseas realizar: "))

        # OPCIONES IMPORTADAS A LAS OPERACIONES.

        if usuario == 1:
            celsius()
        elif usuario == 2:
            fahrenheit()
        elif usuario == 3:
            kelvin()

        # REGRESO AL INDEX PRINCIPAL.

        elif usuario == 4:
            return
    
    # MANEJO DE ERRORES.
    
    except ValueError:
        print("Valor incorrecto, volver a intentar.")
        