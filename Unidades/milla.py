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
        if usuario == 1:
            calculo_valor = float(input("Ingresa el valor en milimetros: "))
            print(f"El valor de milimetros en millas es: {calculo_milimetros(calculo_valor)}")
        elif usuario == 2:
            calculo_valor = float(input("Ingresa el valor en centimetros: "))
            print(f"El valor de centimetros es miilas es: {calculo_centimetros(calculo_valor)}")
        elif usuario == 3:
            calculo_valor = float(input("Ingresa el valor en metros: "))
            print(f"El valor de metros en millas es: {calculo_metros(calculo_valor)}")
        elif usuario == 4:
            calculo_valor = float(input("Ingresa el valor en pulgadas: "))
            print(f"El valor de pulgadas en millas es: {calculo_pulgadas(calculo_pulgadas)}")
        elif usuario == 5:
            print("Proxima funcion")
        elif usuario == 6:
            print("Proxima funcion")
        elif usuario == 7:
            print("Proxima funcion")
    except ValueError:
        print("Error en la digitacion, volver a ingresar un valor valido")