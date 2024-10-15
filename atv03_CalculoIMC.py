def CalculoIMC():
    try:
        peso = float(input("Digite o seu peso (em kg): "))
        altura = float(input("Digite o sua altura (em m): "))
        IMC = peso / (altura ** 2)
        print(f"Seu IMC é: {IMC:.2f}")
        return IMC
    except ValueError:
        print("Valor inválido. Certifique-se de inserir um número válido.")
        return CalculoIMC()
CalculoIMC()