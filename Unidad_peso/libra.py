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
        if usuario == 1:
            calculo_valor = float(input("Ingresa el valor en miligramos: "))
            print(f"El valor de miligramos en libras es: {calculo_miligramos(calculo_valor)} ")
        elif usuario == 2:
            calculo_valor = float(input("Ingresa el valor en gramos: "))
            print(f"El valor de gramos en libras es: {calculo_gramos(calculo_valor)}")
        elif usuario == 3:
            calculo_valor = float(input("Ingresa el valor en kilogramos: "))
            print(f"El valor de los kilogramos en libras es: {calculo_kilogramos(calculo_valor)}")
        elif usuario == 4:
            calculo_valor = float(input("Ingresa el valor en onzas: "))
            print(f"El valor de las onzas en libras es: {calculo_onzas(calculo_valor)}")
    except ValueError:
        print("Error de digitacion, vuelve a intentar")
