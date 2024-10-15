def CalculoMedia():
    try:
        nota1 = float(input("Digite a primeira nota: "))
        nota2 = float(input("Digite a segunda nota: "))
        nota3 = float(input("Digite a terceira nota: "))
        nota4 = float(input("Digite a quarta nota: "))

        media = (nota1 + nota2 + nota3 + nota4) / 4

        if media >= 6:
            print("Aprovado")
        elif media >= 5:
            print("Recuperação")
        else:
            print("Reprovado")
    except ValueError:
        print("Valor inválido. Certifique-se de inserir um número válido.")
    finally:
        print("Fim do programa")
CalculoMedia()        
            