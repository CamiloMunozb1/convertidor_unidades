from temperatura.celsius import celsius
from temperatura.fahrenheit import fahrenheit
from temperatura.kelvin import kelvin


def temperatura():
    print("""
            BIENVENIDO AL CONVERTIDOR DE TEMPERATURAS:
            1. Celsius.
            2. Fahrenheit.
            3. Kelvin.
            4. Atras.
        """)
    try:
        usuario = int(input("Ingresa la operacion que deseas realizar: "))
        if usuario == 1:
            celsius()
        elif usuario == 2:
            fahrenheit()
        elif usuario == 3:
            kelvin()
        elif usuario == 4:
            return
    except ValueError:
        print("Valor incorrecto, volver a intentar.")
        