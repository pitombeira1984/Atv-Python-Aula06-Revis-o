def VerificacaoPolindromo():
    try:
        palavra = input("Digite uma palavra: ")
        palavra = palavra.lower()
        palavraInvertida = palavra[::-1]
        if palavra == palavraInvertida:
            print("A palavra é um palíndromo.")
        else:
            print("A palavra não é um palíndromo.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")        
VerificacaoPolindromo()