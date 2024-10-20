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
        valor_calculo = float(input("Ingresa el valor en milimetros: "))
        if usuario == 1:
            print(f"El valor de milimetros a centimetros es: {operacion_centimetro(valor_calculo)}")
        elif usuario == 2:
            print(f"El valor de milimetros a metros es: {operacion_milimetro(valor_calculo)}")
        elif usuario == 3:
            print(f"El valor de milimetros a pulgadas es: {operacion_pulgadas(valor_calculo)}")
        elif usuario == 4:
            print(f"El valor de milimetros en pies es: {operacion_pies(valor_calculo)}")
        elif usuario == 5:
            print(f"El valor de milimetros en yardas es: {operacion_yardas(valor_calculo)}")
        elif usuario == 6:
            print(f"El valor de milimetros en kilometros es: {operacion_milimetro(valor_calculo)}")
    except ValueError:
        print("Error en la digitacion, volver a ingresar un valor valido")
