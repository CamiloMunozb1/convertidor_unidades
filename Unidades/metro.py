def operacion_milimetros(valor):
    return valor / 1000

def operacion_centimetros(valor):
    return valor / 100

def operacion_pulgada(valor):
    return valor * 0.0254

def operacion_pies(valor):
    return valor * 0.3048

def operacion_yardas(valor):
    return valor * 0.9144

def operacion_kilometros(valor):
    return valor * 1000


def metro():
    print(
        """
            Elige la unidad de medida para realizar la operacion:
            1. Milimetro
            2. Centimetos
            3. Pulgada
            4. Pies
            5. Yardas
            6. Kilometros
        """
        )
    try:
        usuario = int(input("Ingresa la unidad de medida: "))
        valor_calculo = float(input("Ingresa el valor en metros: "))
        if usuario == 1:
            print(f"El valor de metros en milimetros es: {operacion_milimetros(valor_calculo)}")
        elif usuario == 2:
            print(f"El valor de metros en centimetros es: {operacion_centimetros(valor_calculo)}")
        elif usuario == 3:
            print(f"El valor de metros en pulgadas es: {operacion_pulgada(valor_calculo)}")
        elif usuario == 4:
            print(f"El valor de metros en pies es: {operacion_pies(valor_calculo)}")
        elif usuario == 5:
            print(f"El valor de metros en yardas es: {operacion_yardas(valor_calculo)}")
        elif usuario == 6:
            print(f"El valor de metros en kilometros es: {operacion_kilometros(valor_calculo)}")
    except ValueError:
        print("Error en la digitacion, volver a ingresar un valor valido")

