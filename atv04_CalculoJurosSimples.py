def CalculoJurosSimples():
    try:
        principal = float(input("Digite o valor do principal: "))
        taxa = float(input("Digite a taxa de juros ao mês: "))
        tempo = float(input("Digite o tempo em meses: "))
        juros = principal * taxa * tempo
        print(f"O valor dos juros é: {juros:.2f}")
        print(f"O valor total é: {principal + juros:.2f}")
    except ValueError:
        print("Erro: valor inválido")
CalculoJurosSimples()    