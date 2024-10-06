def milimetro():
    print("""
            Elige de que unidad de medida lo quieres realizar:
            1. Centrimetos a Milimetros.
            2. Metros a Milimetros.
            3. Pulgadas a Milimetros.
            """)
    try:
        usuario=int(input("Ingresa la unidad de medida: "))
        if usuario == 1:
            calculo = float(input("Ingresa el centimetro: "))
            convertidor = calculo*10
            print(f"El valor de centimetros a milimetros es: {convertidor}")
        elif usuario == 2:
            calculo = float(input("Ingresa el metros: "))
            convertidor = calculo*1000
            print(f"El valor de metros a milimetros es {convertidor}")
        elif usuario == 3:
            calculo = float(input("ingresa las pulgadas:  "))
            convertidor = calculo*25.4
            print(f"El valor de pulgadas a milimetros es {convertidor}")
    except ValueError:
        print("Error de digitacion, volver a intentar")
