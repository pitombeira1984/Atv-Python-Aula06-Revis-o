def CalculoDesconto():
    try:
        preco = float(input("Digite o preço do produto: "))
        desconto = float(input("Digite o desconto do produto: "))
        preco_desconto = preco - (preco * desconto / 100)
        print(f"O preço do produto com desconto é: {preco_desconto:.2f}")
    except ValueError:
        print("Valor inválido. Certifique-se de inserir um número válido.")
        CalculoDesconto()
CalculoDesconto()     