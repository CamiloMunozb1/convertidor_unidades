def calculo_miligramos(valor):
    return valor / 453_595.37

def calculo_gramos(valor):
    return valor / 453.59237

def calculo_kilogramos(valor):
    return valor * 2.20462

def calculo_onzas(valor):
    return valor / 16


def libras():
    print("""
            Elige la operacion a realizar:
            1. Miligramos.
            2. Gramo.
            3. Kilogramo.
            4. Onza.
        """)
    try:
        usuario = int(input("Ingresa la operacion que deseas hacer: "))
        calculo_valor = float(input("Ingresa el valor en libras: "))
        if usuario == 1:
            print(f"El valor de libras en miligramos es: {calculo_miligramos(calculo_valor)} ")
        elif usuario == 2:
            print(f"El valor de libras en gramos es: {calculo_gramos(calculo_valor)}")
        elif usuario == 3:
            print(f"El valor de libras en kilogramos es: {calculo_kilogramos(calculo_valor)}")
        elif usuario == 4:
            print(f"El valor de libras en onzas es: {calculo_onzas(calculo_valor)}")
    except ValueError:
        print("Error de digitacion, vuelve a intentar")
