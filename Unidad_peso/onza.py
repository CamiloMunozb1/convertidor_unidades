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
        calculo_valor = float(input("Ingresa el valor en onzas: "))
        if usuario == 1:
            print(f"El valor de onzas en miligramos es: {calculo_miligramo(calculo_valor)}")
        elif usuario == 2:
            print(f"El valor de onzas en gramos es: {calculo_gramo(calculo_valor)}")
        elif usuario == 3:
            print(f"El valor de onzas en kilogramos es: {calculo_kilogramo(calculo_valor)}")
        elif usuario == 4:
            print(f"El valor de onzas en libras es: {calculo_libra(calculo_valor)}")
    except ValueError:
        print("Error de digitacion, volver a intentar.")