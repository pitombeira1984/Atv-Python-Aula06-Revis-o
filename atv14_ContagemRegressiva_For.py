def ContagemRegressiva():
    try:
        print("Contagem Regressiva")
        numero = int(input("Digite um número inteiro positivo: "))
        if numero < 0:
            print("Por favor, digite um número inteiro positivo.")
            return
        for i in range(numero, 0, -1):
            print(i)
    except ValueError:
        print("Por favor, digite um número inteiro válido.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
ContagemRegressiva()
            
            
            
            