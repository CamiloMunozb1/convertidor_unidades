def operacion_centimetro(valor):
    return valor * 10

def operacion_milimetro(valor):
    return valor * 1000

def operacion_pulgadas(valor):
    return valor * 25.4

def operacion_pies(valor):
    return valor * 304.8 

def operacion_yardas(valor):
    return valor * 914.4

def operacion_kilometros(valor):
    return valor * 1_000_0000



def milimetro():
    print(
        """
            Elige la unidad de medida para realizar la operacion:
            1. Centrimetos a Milimetros.
            2. Metros a Milimetros.
            3. Pulgadas a Milimetros.
            4. Pies a Milimetros.
            5. Yardas a Milimetros.
            6. Kilometos a Milimetros.
        """)
    try:
        usuario=int(input("Ingresa la unidad de medida: "))
        if usuario == 1:
            valor_calculo = float(input("Ingresa el valor en centimetros: "))
            print(f"El valor de centimetros a milimetros es: {operacion_centimetro(valor_calculo)}")
        elif usuario == 2:
            valor_calculo = float(input("Ingresa el valor en metros: "))
            print(f"El valor de metros a milimetros es: {operacion_milimetro(valor_calculo)}")
        elif usuario == 3:
            valor_calculo = float(input("ingresa el valor en pulgadas:  "))
            print(f"El valor de pulgadas a milimetros es: {operacion_pulgadas(valor_calculo)}")
        elif usuario == 4:
            valor_calculo = float(input("Ingresa el valor en pies:  "))
            print(f"El valor de pies en milimetros es: {operacion_pies(valor_calculo)}")
        elif usuario == 5:
            valor_calculo = float(input("Ingresa el valor en yardas: "))
            print(f"El valor de yardas en milimetros es: {operacion_yardas(valor_calculo)}")
        elif usuario == 6:
            valor_calculo = float(input("Ingresa el valor en Kilometros:  "))
            print(f"El valor de Kilometros en milimetros es: {operacion_milimetro(valor_calculo)}")
    except ValueError:
        print("Error en la digitacion, volver a ingresar un valor valido")
