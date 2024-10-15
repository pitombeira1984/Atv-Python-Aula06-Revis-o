def MetrosEmCentimetro():
    try:
        metros = float(input("Digite o valor em metros: "))
        centimetros = metros * 100
        print(f"{metros} metros equivalem a {centimetros} centímetros.")
    except ValueError:
        print("Valor inválido. Certifique-se de inserir um número válido.")
        
MetrosEmCentimetro()        
        