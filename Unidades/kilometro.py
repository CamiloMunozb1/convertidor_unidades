def operacion_milimetros(valor):
    return valor * 1_000_000

def operacion_centimetros(valor):
    return valor * 100_000

def operacion_metros(valor):
    return valor * 1000

def operacion_pulgadas(valor):
    return valor * 0.0000254

def operacion_pies(valor):
    return valor * 0.0003048

def operacion_yardas(valor):
    return valor * 0.0009144

def kilometro():
    print(
        """
            Elige la unidad de medida para realizar la operacion:
            1. Milimetros
            2. Centimetros
            3. Metros
            4. Pulgadas
            5. Pies
            6. Yardas
        """
        )
    try:
        usuario = int(input("Ingresa la unidad de medida: "))
        if usuario == 1:
            valor_calculo = float(input("Ingresa el valor en milimetros: "))
            print(f"El valor de milimetros en kilometros es: {operacion_milimetros(valor_calculo)}")
        elif usuario == 2:
            valor_calculo = float(input("Ingresa el valor en centimetros: "))
            print(f"El valor de centimetros en Kilometros es: {operacion_centimetros(valor_calculo)}")
        elif usuario == 3:
            valor_calculo = float(input("Ingresa el valor en metros: "))
            print(f"El valor de metros en kilometros es: {operacion_metros(valor_calculo)}")
        elif usuario == 4:
            valor_calculo = float(input("Ingresa el valor en pulgadas: "))
            print(f"El valor de pulgadas en kilometros es: {operacion_pulgadas(valor_calculo)}")
        elif usuario == 5:
            valor_calculo = float(input("Ingresa el valor en pies: "))
            print(f"El valor de los pies en kilometros es: {operacion_pies(valor_calculo)}")
        elif usuario == 6:
            valor_calculo = float(input("Ingresa el valor en yardas: "))
            print(f"El valor de las yardas en kilometros es {operacion_yardas(valor_calculo)}")
    except ValueError:
        print("Error en la digitacion, volver a ingresar un valor valido")