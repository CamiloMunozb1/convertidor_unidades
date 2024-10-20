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
        valor_calculo = float(input("Ingresa el valor en kilometros: "))
        if usuario == 1:
            print(f"El valor de kilometros en milimetros es: {operacion_milimetros(valor_calculo)}")
        elif usuario == 2:
            print(f"El valor de kilometros en centimetros es: {operacion_centimetros(valor_calculo)}")
        elif usuario == 3:
            print(f"El valor de kilometros en metros es: {operacion_metros(valor_calculo)}")
        elif usuario == 4:
            print(f"El valor de kilometros en pulgadas es: {operacion_pulgadas(valor_calculo)}")
        elif usuario == 5:
            print(f"El valor de kilometros en pies es: {operacion_pies(valor_calculo)}")
        elif usuario == 6:
            print(f"El valor de kilometros en yardas es: {operacion_yardas(valor_calculo)}")
    except ValueError:
        print("Error en la digitacion, volver a ingresar un valor valido")