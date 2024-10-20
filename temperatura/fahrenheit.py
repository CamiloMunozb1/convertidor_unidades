def calculo_celsius(valor):
    return (valor - 32) * 0.5556

def calculo_kelvin(valor):
    return (valor - 32) * 0.5556 + 273.15


def fahrenheit():
    print("""
            Elige la operacion a realizar:
            1. Celsius.
            2. Kelvin
        """)
    try:
        usuario = int(input("Ingresa que conversion deseas realizar: "))
        calculo_valor = float(input("Ingresa el valor en Fahrenheit: "))
        if usuario == 1:
            print(f"El valor de Fahrenheit en celsius es: {calculo_celsius(calculo_valor)}")
        elif usuario == 2: 
            print(f"El valor de Fahrenheit en kelvin es: {calculo_kelvin(calculo_valor)}")
    except ValueError:
        print("Error de digitacion, volver a ingresar una entrada valida.")
