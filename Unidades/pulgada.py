def calculo_milimetros(valor):
    return valor / 25.4

def calculo_centimetros(valor):
    return valor / 2.54

def calculo_metros(valor):
    return valor * 39.3701

def calculo_pies(valor):
    return valor * 12

def calculo_yardas(valor):
    return valor * 36

def calculo_kilometro(valor):
    return valor * 39_370_1


def pulgada():
    print(
        """
            Elige la unidad de medida para realizar la operacion:
            1. Milimetros.
            2. Centimetros.
            3. Metros.
            4. Pies.
            5. Yardas.
            6. Kilometro.
        """
    )
    try:
        usuario = int(input("Ingresa la unidad de medida: "))
        valor_calculo = float(input("Ingresa el valor en pulgadas"))
        if usuario == 1:
            print(f"El valor de pulgadas en milimetros es: {calculo_milimetros(valor_calculo)}")
        elif usuario == 2:
            print(f"El valor de pulgadas en centimetros es: {calculo_centimetros(valor_calculo)}")
        elif usuario == 3:
            print(f"El valor de pulgadas en metros es: {calculo_metros(valor_calculo)}")
        elif usuario == 4:
            print(f"El valor de pulgadas en pies es: {calculo_yardas(valor_calculo)}")
        elif usuario == 5:
            print(f"El valor de pulgadas en yardas es: {calculo_yardas(valor_calculo)}")
        elif usuario == 6:
            print(f"El valor de pulgadas en kilometros es: {calculo_kilometro(valor_calculo)} ")
    except ValueError:
        print("Error en la digitacion, volver a ingresar un valor valido")