def tabuadanumero():
    try:
        numero = int(input("Digite um número para ver sua tabuada: "))

        print(f"Tabuada do {numero}:")
        for i in range(1, 11):  
            resultado = numero * i  
            print(f"{numero} x {i} = {resultado}")  
    except ValueError:
        print("Por favor, digite um número válido.")
        
tabuadanumero()