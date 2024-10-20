def operacion_milimetros(valor):
    return valor / 10

def operacion_metros(valor):
    return valor * 100

def operacion_pulgadas(valor):
    return valor * 2.54

def operacion_pies(valor):
    return valor * 30.48

def operacion_yardas(valor):
    return valor * 91.44

def operacion_kilometros(valor):
    return valor * 100_000


def centimetro():
    print(
        """
            Elige la unidad de medida para realizar la operacion:
            1. Milimetros
            2. Metros
            3. Pulgadas
            4. Pies
            5. Yardas
            6. Kilometros
        """
        )
    try:
        usuario = int(input("ingresa la unidad de medida: "))
        valor_calculo = float(input("Ingresa el valor en centimetros: "))
        if usuario == 1:
            print(f"el valor de centimetros en milimetros es: {operacion_milimetros(valor_calculo)}")
        elif usuario == 2:
            print(f"El valor de centimetros en metros es: {operacion_metros(valor_calculo)} ")
        elif usuario == 3:
            print(f"El valor de centimetros en pulgadas es: {operacion_pulgadas(valor_calculo)}")
        elif usuario == 4:
            print(f"El valor de los centimetros en pies es: {operacion_pies(valor_calculo)}")
        elif usuario == 5:
            print(f"El valor de las centimetros en yardas es: {operacion_yardas(valor_calculo)}")
        elif usuario == 6:
            print(f"El valor de los centimetros en kilometros es: {operacion_kilometros(valor_calculo)}")
    except ValueError:
        print("Error en la digitacion, volver a ingresar un valor valido")