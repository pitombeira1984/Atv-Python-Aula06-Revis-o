def SomaNumerosPares():
    try:
        numero = int(input("Digite um número inteiro: "))
        contador = 0
        soma = 0
        while contador <= numero:
            if contador % 2 == 0:
                print(contador)
                soma += contador
            contador += 1
        print(f'A soma do numeros pares é: {soma}')    
    except ValueError:
        print("Valor inválido. Certifique-se de inserir um número válido.")
SomaNumerosPares()            
                