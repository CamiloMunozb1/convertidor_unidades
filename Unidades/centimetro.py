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
        if usuario == 1:
            valor_calculo = float(input("Ingresa el valor en milimetros: "))
            print(f"el valor de milimetros en centimetros es: {operacion_milimetros(valor_calculo)}")
        elif usuario == 2:
            valor_calculo = float(input("Ingresa el valor en metros: "))
            print(f"El valor de metros en centimetos es: {operacion_metros(valor_calculo)} ")
        elif usuario == 3:
            valor_calculo = float(input("Ingresa el valor en pulgadas: "))
            print(f"El valor de las pulgadas en centimetros es: {operacion_pulgadas(valor_calculo)}")
        elif usuario == 4:
            valor_calculo = float(input("Ingresa el valor en pies: "))
            print(f"El valor de los pies en centimetros es: {operacion_pies(valor_calculo)}")
        elif usuario == 5:
            valor_calculo = float(input("Ingresa el valror en pies: "))
            print(f"El valor de las yardas en centimetros es: {operacion_yardas(valor_calculo)}")
        elif usuario == 6:
            print(f"El valor de los kilometros en centimetros es: {operacion_kilometros(valor_calculo)}")
    except ValueError:
        print("Error en la digitacion, volver a ingresar un valor valido")