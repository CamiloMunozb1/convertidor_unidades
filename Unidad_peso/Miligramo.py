def operacion_gramo(valor):
    return valor / 1000

def operacion_kilogramos(valor):
    return valor / 1_000_000

def operacipn_onzas(valor):
    return valor / 28_349_52

def operacion_libras(valor):
    return valor / 453_592_37


def miligramos():
    print(
        """
            Elige la operacion a realizar:
            1. Gramo.
            2. Kilogramos.
            3. Onzas.
            4. Libras.
        """
    )
    try:
        usuario = int(input("Ingresa de que medida va ser la conversion: "))
        if usuario == 1:
            valor_calculo = float(input("Ingresa el valor en Gramos: "))
            print(f"El valor del gramos a Miligramos es: {operacion_gramo(valor_calculo)}")
        elif usuario == 2:
            valor_calculo = float(input("Ingresa el valor en kilogramos: "))
            print(f"El valor del kilogramo a Miligramo es: {operacion_kilogramos(valor_calculo)}")
        elif usuario == 3:
            valor_calculo = float(input("Ingesa el valor en Onzas: "))
            print(f"El valor de las Onzas en Miligramos es: {operacipn_onzas(valor_calculo)}")
        elif usuario == 4:
            valor_calculo = float(input("Ingresa el valor en Libras: "))
            print(f"El valor de las libras en Miligramos es: {operacion_libras(valor_calculo)}")
    except ValueError:
        print("Error de digitacion, volver a intentar.")