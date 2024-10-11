def calculo_milimetro(valor):
    return valor / 304.8

def calculo_centimetros(valor):
    return valor / 30.48

def calculo_metros(valor):
    return valor * 3.28084

def calculo_pulgadas(valor):
    return valor / 12

def calculo_yardas(valor):
    return valor * 3

def calculo_kilometros(valor):
    return valor * 3280.84


def pies():
    print(
        """
            Elige la unidad de medida para realizar la operacion:
            1. Milimetro.
            2. Centimetro.
            3. Metros.
            4. Pulgadas.
            5. Yardas.
            6. Kilometros.
        """
        )
    try:
        usuario = int(input("Ingresa la unidad de medida: "))
        if usuario == 1:
            valor_calculo = float(input("Ingresa el valor en milimetros: "))
            print(f"El valor de  milimetros en pies es: {calculo_milimetro(valor_calculo)}")
        elif usuario == 2:
            valor_calculo = float(input("Ingresa el valor en centimetros: "))
            print(f"El valor de centimetros en pies es: {calculo_centimetros(valor_calculo)}")
        elif usuario == 3:
            valor_calculo = float(input("Ingresa el valor en metros: "))
            print(f"El valor de metros en pies es: {calculo_metros(valor_calculo)}")
        elif usuario == 4:
            valor_calculo = float(input("Ingresa el valor en pulgadas: "))
            print(f"El valor de pulgadas en pies es: {calculo_pulgadas(valor_calculo)}")
        elif usuario == 5:
            valor_calculo = float(input("Ingresa el valor en yardas: "))
            print(f"El valor de yardas en pies es {calculo_yardas(valor_calculo)}")
        elif usuario == 6:
            valor_calculo = float(input("Ingresa el valor en Kilometros: "))
            print(f"El valor de Kilometros en pies es: {calculo_kilometros(valor_calculo)}")
    except ValueError:
        print("Error en la digitacion, volver a ingresar un valor valido")