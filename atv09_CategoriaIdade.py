def CategoriaIdade():
    try:
        idade = int(input("Digite sua idade: "))
        if idade < 0:
            print("Idade inválida.")
        elif idade < 12:
            print("Você é Criança.")
        elif idade > 12  and idade < 18:
            print("Você é um adolescente.")
        elif idade >= 18 and idade <= 60:
            print("Você é um adulto.")
        else:
            print("Você é um idoso.")
    except ValueError:
        print("Valor inválido. Certifique-se de inserir um número válido.")
        CategoriaIdade()
    finally:
        print("Fim do programa.")
CategoriaIdade()