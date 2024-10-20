def operacion_miligramo(valor):
    return valor * 1000

def operacion_kilogramo(valor):
    return valor / 1000

def operacion_onza(valor):
    return valor / 28.3495

def operacion_libra(valor):
    return valor / 453.592


def gramo():
    print("""
            Elige la operacion a realizar:
            1. Miligramo.
            2.Kilogramo.
            3.Onza.
            4.Libra.
        """)
    try:
        usuario = int(input("Ingresa de que medida va ser la conversion: "))
        calculo_valor = float(input("Ingresa el valor en gramos: "))
        if usuario == 1:
            print(f"El valor de gramos en miligramos es: {operacion_miligramo(calculo_valor)}")
        elif usuario == 2:
            print(f"El valor de gramos en kilogramos es: {operacion_kilogramo(calculo_valor)}")
        elif usuario == 3:
            print(f"El valor de gramos en onzas es: {operacion_onza(calculo_valor)}")
        elif usuario == 4:
            print(f"El valor de gramos en libras es: {operacion_libra(calculo_valor)}")
    except ValueError:
        print("Error de digitacion, volver a intentar.")
