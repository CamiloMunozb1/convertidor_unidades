def calculo_milimetros(valor):
    return valor / 1_609_344

def calculo_centimetros(valor):
    return valor / 160_934_4

def calculo_metros(valor):
    return valor / 1609.344

def calculo_pulgadas(valor):
    return valor / 63.360

def calculo_pies(valor):
    return  valor / 5280

def calculo_yardas(valor):
    return valor / 1760

def calculo_kilometros(valor):
    return valor / 1.609344


def millas():
    print(
        """
            Elige la unidad de medida para realizar la operacion:
            1. Milimetros.
            2. Centimetros.
            3. Metros.
            4. Pulgadas.
            5. Pies.
            6. Yardas.
            7. Kilometros.
        """
    )
    try:
        usuario = int(input("Ingresa la unidad de medida: "))
        calculo_valor = float(input("Ingresa el valor en millas: "))
        if usuario == 1:
            print(f"El valor de millas en milimetros es: {calculo_milimetros(calculo_valor)}")
        elif usuario == 2:
            print(f"El valor de millas en centimetros es: {calculo_centimetros(calculo_valor)}")
        elif usuario == 3:
            print(f"El valor de millas en metros es: {calculo_metros(calculo_valor)}")
        elif usuario == 4:
            print(f"El valor de millas en pulgadas es: {calculo_pulgadas(calculo_pulgadas)}")
        elif usuario == 5:
            print(f"El valor de millas en pies es: {calculo_pies(calculo_valor)}")
        elif usuario == 6:
            print(f"El valor de millas en yardas es: {calculo_yardas(calculo_valor)}")
        elif usuario == 7:
            print(f"El valor de millas en Kilometros es: {calculo_kilometros(calculo_valor)}")
    except ValueError:
        print("Error en la digitacion, volver a ingresar un valor valido")