def calculo_milimetro(valor):
    return valor * 914.4

def calculo_centimetros(valor):
    return valor / 91.44

def calculo_metros(valor):
    return valor * 1.09361

def calculo_pulgadas(valor):
    return valor / 36

def calculo_pies(valor):
    return valor / 3

def calculo_kilometros(valor):
    return valor * 1093.61


def yardas():
    print(
        """
            Elige la unidad de medida para realizar la operacion:
            1. Milimetro.
            2. Centimetros.
            3. Metros.
            4. Pulgadas.
            5. Pies.
            6. Kilometros.
        """
    )
    try:
        usuario = int(input("Ingresa la unidad de medida: "))
        calculo_valor = float(input("Ingresa el valor en yardas: "))
        if usuario == 1:
            print(f"El valor de yardas en milimetros es: {calculo_milimetro(calculo_valor)}")
        elif usuario == 2:
            print(f"El valor de yardas en centimetros es: {calculo_centimetros(calculo_valor)}")
        elif usuario == 3:
            print(f"El valor de yardas en metros es: {calculo_metros(calculo_valor)}")
        elif usuario == 4:
            print(f"El valor de yardas en pulgadas es: {calculo_pulgadas(calculo_valor)}")
        elif usuario == 5:
            print(f"El valor de yardas en pies es: {calculo_pies(calculo_valor)}")
        elif usuario == 6:
            print(f"El valor de yardas en kilometros es: {calculo_kilometros(calculo_valor)}")
    except ValueError:
        print("Error en la digitacion, volver a ingresar un valor valido")