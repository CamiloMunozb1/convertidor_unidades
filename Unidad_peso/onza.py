def calculo_miligramo(valor):
    return valor * 28_349_5

def calculo_gramo(valor):
    return valor * 28.3495

def calculo_kilogramo(valor):
    return valor / 35.274

def calculo_libra(valor):
    return valor / 16


def onza():
    print("""
            Elige la operacion a realizar:
            1. Miligramo.
            2. Gramo.
            3. Kilogramo.
            4. Libra.
        """)
    try:
        usuario = int(input("Ingresa la operacion que deseas hacer: "))
        if usuario == 1:
            calculo_valor = float(input("Ingresa el valor en miligramos: "))
            print(f"El valor de Miligramos en Onzas es: {calculo_miligramo(calculo_valor)}")
        elif usuario == 2:
            calculo_valor = float(input("Ingresa el valor en gramos: "))
            print(f"El valor de Gramos en Onzas es: {calculo_gramo(calculo_valor)}")
        elif usuario == 3:
            calculo_valor = float(input("Ingresa el valor en kilogramos: "))
            print(f"El valor de Kilogramos en Onzas es: {calculo_kilogramo(calculo_valor)}")
        elif usuario == 4:
            calculo_valor = float(input("Ingresa el valor en libras: "))
            print(f"El valor en Libras en Onzas es: {calculo_libra(calculo_valor)}")
    except ValueError:
        print("Error de digitacion, volver a intentar.")