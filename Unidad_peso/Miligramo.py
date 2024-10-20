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
        valor_calculo = float(input("Ingresa el valor en miligramos: "))
        if usuario == 1:
            print(f"El valor de miligramos a gramos es: {operacion_gramo(valor_calculo)}")
        elif usuario == 2:
            print(f"El valor de miligramos a kilogramos es: {operacion_kilogramos(valor_calculo)}")
        elif usuario == 3:
            print(f"El valor de miligramos en onzas es: {operacipn_onzas(valor_calculo)}")
        elif usuario == 4:
            print(f"El valor de miligramos en libras es: {operacion_libras(valor_calculo)}")
    except ValueError:
        print("Error de digitacion, volver a intentar.")