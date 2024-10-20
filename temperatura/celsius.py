def calculo_fahrenheit(valor):
    return (valor * 1.8) + 32

def calculo_kelvin(valor):
    return valor + 273.15


def celsius():
    print("""
            Elige la operacion a realizar:
            1. Fahrenheit.
            2. Kelvin.
        """)
    try:
        usuario = int(input("Ingresa conversion a realizar: "))
        calculo_valor = float(int("Ingresa el valor en celsius: "))
        if usuario == 1:
            print(f"El valor de celsius en Fahrenheit es: {calculo_fahrenheit(calculo_valor)}")
        elif usuario == 2:
            print(f"EL valor de celsius en Kelvin es: {calculo_kelvin(calculo_valor)}")
    except ValueError:
        print("Error de digitacion, volver a ingresar una entrada valida.")