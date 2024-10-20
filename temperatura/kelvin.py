def calculo_celsius(valor):
    return valor - 273.15

def calculo_fahrenheit(valor):
    return (valor - 273.15) * 1.8 + 32


def kelvin():
    print("""
            Elige la operacion a realizar:
            1. Celsius.
            2. Fahrenheit.
        """)
    try:
        usuario = int(input("Ingresa la conversion que deseas realizar: "))
        calculo_valor = float(input("Ingresa el valor en Kelvin: "))
        if usuario == 1:
            print(f"El valor de Kelvin en Celsius es: {calculo_celsius(calculo_valor)}")
        elif usuario == 2:
            print(f"El valor de Kelvin en Fahrenheit es: {calculo_fahrenheit(calculo_valor)}")
    except ValueError:
        print("Error de digitacion, volver a ingresar una entrada valida.")