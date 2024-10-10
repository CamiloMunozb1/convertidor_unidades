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
        if usuario == 1:
            valor_calculo = float(input("Ingresa el valor en milimetros: "))
            print(f"El valor de milimetros en metros es {operacion_milimetros(valor_calculo)}")
        elif usuario == 2:
            valor_calculo = float(input("Ingresa el valor en centimetros: "))
            print(f"El valor de centimetros en metros es {operacion_centimetros(valor_calculo)}")
        elif usuario == 3:
            valor_calculo = float(input("Ingresa el valor en pulgadas: "))
            print(f"El valor de pulgadas en metros es {operacion_pulgada(valor_calculo)}")
        elif usuario == 4:
            valor_calculo = float(input("Ingresa el valor en pies: "))
            print(f"El valor de pies en metros es {operacion_pies(valor_calculo)}")
        elif usuario == 5:
            valor_calculo = float(input("Ingresa el valor en yardas: "))
            print(f"El valor de yardas en metros es {operacion_yardas(valor_calculo)}")
        elif usuario == 6:
            valor_calculo = float(input("Ingresa el valor en kilometros: "))
            print(f"El valor de kilometros en metros es {operacion_kilometros(valor_calculo)}")
    except ValueError:
        print("Error en la digitacion, volver a ingresar un valor valido")

