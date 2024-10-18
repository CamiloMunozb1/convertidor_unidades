def calculo_miligramo(valor):
    return valor * 1_000_000

def calculo_gramo(valor):
    return valor * 1000

def calculo_onza(valor):
    return valor * 35.274

def calculo_libra(valor):
    return valor * 2.20462


def kilogramo():
    print("""
            Elige la operacion a realizar:
            1. Miligramo.
            2. Gramo.
            3. Onza.
            4. Libra.
        """)
    try:
        usuario = int(input("Ingresa de que medida va ser la conversion: "))
        if usuario == 1:
            valor_calculo = float(input("Ingresa el valor en miligramo: "))
            print(f"El valor del miligramo en kilogramo es: {calculo_miligramo(calculo_miligramo)}")
        elif usuario == 2:
            valor_calculo = float(input("Ingresa el valor en gramos: "))
            print(f"El valor de los gramos en kilogramos es: {calculo_gramo(valor_calculo)}")
        elif usuario == 3:
            valor_calculo = float(input("Ingresa el valor en onzas: "))
            print(f"El valor de las onzas en kilogramos es: {calculo_onza(valor_calculo)}")
        elif usuario == 4:
            valor_calculo = float(input("Ingresa el valor en libras: "))
            print(f"El valor de las libras en kilogramos es: {calculo_libra(valor_calculo)}")
    except ValueError:
        print("Error de digitacion, volver a intentar.")
